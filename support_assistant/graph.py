from typing import TypedDict

import chromadb
from sentence_transformers import SentenceTransformer
from langgraph.graph import StateGraph, START, END
from support_assistant.config import MOCK_LLM


# -----------------------------
# 1. Load embedding model
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# 2. Connect to ChromaDB
# -----------------------------
client = chromadb.PersistentClient(
    path="./support_assistant/chroma_db"
)

collection = client.get_collection(
    name="zepto_policies",
    embedding_function=None
)


# -----------------------------
# 3. Define graph state
# -----------------------------
class SupportState(TypedDict):
    query: str
    intent: str
    answer: str
    sources: list[str]
    confidence: float


# -----------------------------
# 4. Node: classify_intent
# -----------------------------
def classify_intent(state: SupportState):

    query = state["query"].lower()

    policy_keywords = [
        "delivery",
        "return",
        "refund",
        "membership",
        "tracking",
        "cancel",
        "gift card",
        "support hours",
    ]

    if any(keyword in query for keyword in policy_keywords):
        intent = "policy_question"
    else:
        intent = "general_question"

    return {
        "intent": intent
    }


# -----------------------------
# 5. Node: retrieve_and_answer
# -----------------------------
def retrieve_and_answer(state: SupportState):

    query = state["query"]

    # Create query embedding
    query_embedding = model.encode([query]).tolist()

    # Retrieve top 3 documents
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )

    # Get most similar document
    top_document = results["documents"][0][0]
    top_id = results["ids"][0][0]

    # Short excerpt (~200 characters)
    top_chunk_snippet = top_document[:200]

    # Deterministic mock answer
    answer = f"Based on the retrieved context: {top_chunk_snippet}"

    return {
        "answer": answer,
        "sources": [top_id],
        "confidence": 1.0,
    }


# -----------------------------
# 6. Node: direct_answer
# -----------------------------
def direct_answer(state: SupportState):

    # Retrieval also runs for general questions as required.
    query = state["query"]
    query_embedding = model.encode([query]).tolist()

    collection.query(
        query_embeddings=query_embedding,
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )

    # The retrieved context is intentionally not used
    # because this is a general-question mock response.
    return {
        "answer": "I can only answer questions about Zepto policies right now.",
        "sources": [],
        "confidence": 1.0,
    }

# -----------------------------
# 7. Conditional routing
# -----------------------------
def route_question(state: SupportState):

    if state["intent"] == "policy_question":
        return "retrieve_and_answer"

    return "direct_answer"


# -----------------------------
# 8. Build LangGraph
# -----------------------------
builder = StateGraph(SupportState)

builder.add_node(
    "classify_intent",
    classify_intent
)

builder.add_node(
    "retrieve_and_answer",
    retrieve_and_answer
)

builder.add_node(
    "direct_answer",
    direct_answer
)

builder.add_edge(
    START,
    "classify_intent"
)

builder.add_conditional_edges(
    "classify_intent",
    route_question,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer",
    }
)

builder.add_edge(
    "retrieve_and_answer",
    END
)

builder.add_edge(
    "direct_answer",
    END
)


# Compile graph
graph = builder.compile()
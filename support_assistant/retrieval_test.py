import chromadb
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="./support_assistant/chroma_db"
)

collection = client.get_collection(
    name="zepto_policies",
    embedding_function=None
)


# User query
query = "How much is the delivery fee for orders below INR 149?"


# Create query embedding
query_embedding = model.encode([query]).tolist()


# Retrieve top 3 similar documents
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3,
    include=["documents", "metadatas", "distances"]
)


# Display results
print("\nQUERY:")
print(query)

print("\nRETRIEVED DOCUMENTS:")

for i in range(len(results["ids"][0])):
    print("\n-----------------------------")
    print("ID:", results["ids"][0][i])
    print("Source:", results["metadatas"][0][i])
    print("Distance:", results["distances"][0][i])
    print("Document:")
    print(results["documents"][0][i])
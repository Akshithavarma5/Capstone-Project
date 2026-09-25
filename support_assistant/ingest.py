from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


# Paths
BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
CHROMA_DIR = BASE_DIR / "chroma_db"


# Load the embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Embedding model loaded successfully.")


# Create persistent ChromaDB client
client = chromadb.PersistentClient(path=str(CHROMA_DIR))

# Create or get the collection
collection = client.get_or_create_collection(
    name="zepto_policies",
    metadata={"description": "Zepto support policy documents"}
)


# Load all 8 documents
documents = []
document_ids = []
metadatas = []

for file_path in sorted(DOCS_DIR.glob("doc_*.txt")):
    text = file_path.read_text(encoding="utf-8").strip()

    documents.append(text)
    document_ids.append(file_path.stem)
    metadatas.append({"source": file_path.name})


print(f"Documents loaded: {len(documents)}")


# Generate embeddings
print("Generating embeddings...")
embeddings = model.encode(documents).tolist()
print("Embeddings generated successfully.")


# Store documents and embeddings in ChromaDB
collection.upsert(
    ids=document_ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)


print("Documents stored in ChromaDB successfully.")
print("Collection name:", collection.name)
print("Number of stored documents:", collection.count())
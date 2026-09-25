# Zepto Support Assistant

## Overview

This project implements a small GenAI-style customer support assistant for Zepto.

The assistant uses:

- Local SentenceTransformer embeddings
- ChromaDB for vector storage and retrieval
- LangGraph for intent routing and workflow orchestration
- Pydantic for validated structured responses
- FastAPI for the `/ask` API
- A deterministic mock LLM path that requires no API key or network access

The mock mode is the default and is controlled using the `MOCK_LLM` environment variable.

---

## Project Structure

```text
support_assistant/
├── chroma_db/
├── docs/
│   ├── doc_01.txt
│   ├── doc_02.txt
│   ├── doc_03.txt
│   ├── doc_04.txt
│   ├── doc_05.txt
│   ├── doc_06.txt
│   ├── doc_07.txt
│   └── doc_08.txt
├── config.py
├── Dockerfile
├── graph.py
├── ingest.py
├── main.py
├── prompt.py
├── requirements.txt
├── retrieval_test.py
└── schemas.py

## Development Workflow

Changes are developed on feature branches, reviewed, and merged into the main branch.
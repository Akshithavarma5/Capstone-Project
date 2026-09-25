from fastapi import FastAPI
from pydantic import BaseModel

from support_assistant.graph import graph
from support_assistant.schemas import SupportResponse


app = FastAPI(title="Zepto Support Assistant")


class AskRequest(BaseModel):
    query: str


@app.post("/ask", response_model=SupportResponse)
def ask(request: AskRequest):

    result = graph.invoke({
        "query": request.query,
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0,
    })

    return SupportResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"],
    )
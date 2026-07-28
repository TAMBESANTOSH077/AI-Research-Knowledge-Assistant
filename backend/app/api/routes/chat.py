from fastapi import APIRouter
from pydantic import BaseModel
from app.core.history_store import save_chat

from app.rag.qa import ask_question

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):
    result = ask_question(request.question)

    save_chat(
        request.question,
        result["answer"]
    )

    return result
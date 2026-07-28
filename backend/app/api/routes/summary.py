from fastapi import APIRouter

from app.rag.summarizer import summarize_document

router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)

@router.get("/")
def summary():
    return summarize_document()
from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.comparator import compare_documents

router = APIRouter(
    prefix="/compare",
    tags=["Compare"]
)


class CompareRequest(BaseModel):
    question: str


@router.post("/")
def compare(request: CompareRequest):
    return compare_documents(request.question)
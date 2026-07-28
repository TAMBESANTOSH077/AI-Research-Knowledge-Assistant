from pathlib import Path
from fastapi import APIRouter
from app.rag.vector_store import vector_store

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

UPLOAD_DIR = Path("data/uploads")


@router.get("/")
async def analytics():

    docs = len(list(UPLOAD_DIR.glob("*")))

    try:
        chunks = vector_store._collection.count()
    except Exception:
        chunks = 0

    return {
        "documents": docs,
        "chunks": chunks,
        "questions": 0,
        "avg_response": "0.00 s",
        "vector_store": "Active"
    }
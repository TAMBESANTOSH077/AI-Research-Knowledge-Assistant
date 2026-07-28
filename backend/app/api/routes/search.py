from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.vector_store import vector_store

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

class SearchRequest(BaseModel):
    query: str


@router.post("/")
async def semantic_search(request: SearchRequest):
    docs = vector_store.similarity_search(
        request.query,
        k=5
    )

    results = []

    for doc in docs:
        results.append({
            "content": doc.page_content,
            "document": doc.metadata.get("document", "Unknown")
        })

    return {
        "results": results
    }
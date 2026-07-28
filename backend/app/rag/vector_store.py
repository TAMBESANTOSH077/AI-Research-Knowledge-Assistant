from pathlib import Path

from langchain_chroma import Chroma
from app.rag.embeddings import embedding_model

VECTOR_DB = Path("data/chroma_db")
VECTOR_DB.mkdir(parents=True, exist_ok=True)

vector_store = Chroma(
    collection_name="research_documents",
    embedding_function=embedding_model,
    persist_directory=str(VECTOR_DB)
)
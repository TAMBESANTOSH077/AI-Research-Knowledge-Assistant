from pathlib import Path

from app.rag.parser import extract_text
from app.rag.chunker import create_chunks
from app.rag.vector_store import vector_store

UPLOAD_DIR = Path("data/uploads")

pdf_files = list(UPLOAD_DIR.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError("No PDF found in data/uploads")

pdf_path = pdf_files[0]

print(f"Indexing: {pdf_path}")

pages = extract_text(str(pdf_path))
chunks = create_chunks(pages)

vector_store.add_documents(chunks)

print(f"Indexed {len(chunks)} chunks successfully!")
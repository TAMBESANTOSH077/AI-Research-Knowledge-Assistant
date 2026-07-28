from pathlib import Path

from app.rag.parser import extract_text
from app.rag.chunker import create_chunks
from app.rag.vector_store import vector_store

UPLOAD_DIR = Path("data/uploads")


def index_documents():
    pdf_files = list(UPLOAD_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError("No PDF found in data/uploads")

    total_documents = 0
    total_chunks = 0

    for pdf_path in pdf_files:
        print("=" * 60)
        print(f"📄 Indexing: {pdf_path.name}")

        # Extract text
        pages = extract_text(str(pdf_path))

        print(f"Pages: {len(pages)}")

        # Create chunks
        chunks = create_chunks(pages)

        print(f"Chunks: {len(chunks)}")

        # Add metadata to every chunk
        for chunk in chunks:
            chunk.metadata["document"] = pdf_path.name

        # Store in ChromaDB
        vector_store.add_documents(chunks)

        print(f"✅ Indexed {len(chunks)} chunks successfully.")

        total_documents += 1
        total_chunks += len(chunks)

    print("\n" + "=" * 60)
    print("🎉 Indexing Completed")
    print(f"Documents Indexed : {total_documents}")
    print(f"Total Chunks      : {total_chunks}")
    print("=" * 60)


if __name__ == "__main__":
    index_documents()
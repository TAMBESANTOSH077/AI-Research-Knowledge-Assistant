from pathlib import Path

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from app.rag.parser import extract_text
from app.rag.chunker import create_chunks
from app.rag.vector_store import vector_store

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    # Save PDF
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text
    pages = extract_text(str(file_path))

    # Create chunks
    chunks = create_chunks(pages)

    # Add metadata
    for chunk in chunks:
        chunk.metadata["document"] = file.filename

    # Remove old vectors if the same document already exists
    try:
        vector_store.delete(
            where={"document": file.filename}
        )
    except Exception:
        pass

    # Index
    vector_store.add_documents(chunks)

    # Debug
    print("Indexed:", len(chunks))
    print("Total vectors:", vector_store._collection.count())

    return JSONResponse(
        {
            "message": "Document uploaded successfully",
            "filename": file.filename,
            "pages": len(pages),
            "chunks": len(chunks),
            "total_vectors": vector_store._collection.count()
        }
    )


@router.get("/files")
async def list_files():
    files = []

    for file in UPLOAD_DIR.glob("*.pdf"):
        files.append(
            {
                "name": file.name,
                "size": round(file.stat().st_size / 1024, 2)
            }
        )

    return {
        "count": len(files),
        "files": files
    }


@router.delete("/files/{filename}")
async def delete_file(filename: str):

    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    file_path.unlink()

    try:
        vector_store.delete(
            where={"document": filename}
        )
    except Exception:
        pass

    return {
        "message": f"{filename} deleted successfully"
    }
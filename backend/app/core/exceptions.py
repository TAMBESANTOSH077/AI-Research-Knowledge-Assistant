from fastapi import HTTPException


def document_not_found():
    raise HTTPException(
        status_code=404,
        detail="Document not found"
    )
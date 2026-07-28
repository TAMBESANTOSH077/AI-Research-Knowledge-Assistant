from pathlib import Path
from fastapi import APIRouter

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.get("/files")
async def get_uploaded_files():
    files = []

    for file in UPLOAD_DIR.iterdir():
        if file.is_file():
            files.append({
                "name": file.name,
                "size": round(file.stat().st_size / 1024, 2)
            })

    return {
        "count": len(files),
        "files": files
    }
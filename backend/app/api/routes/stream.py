from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time

router = APIRouter(
    prefix="/stream",
    tags=["Streaming"]
)

def generate():
    text = (
        "This is a streaming response from your AI Research "
        "Knowledge Assistant."
    )

    for word in text.split():
        yield word + " "
        time.sleep(0.05)


@router.get("/")
def stream():
    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )
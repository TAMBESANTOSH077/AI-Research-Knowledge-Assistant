from pydantic import BaseModel
from datetime import datetime


class UploadResponse(BaseModel):
    id: int
    document_name: str
    total_pages: int
    processing_status: str
    upload_time: datetime
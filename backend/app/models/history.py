from pydantic import BaseModel
from datetime import datetime


class ChatHistory(BaseModel):
    question: str
    answer: str
    timestamp: datetime
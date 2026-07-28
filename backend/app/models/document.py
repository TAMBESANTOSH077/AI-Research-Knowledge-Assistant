from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.base import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    document_name = Column(String, nullable=False)

    file_path = Column(String)

    upload_time = Column(DateTime, default=datetime.utcnow)

    total_pages = Column(Integer)

    total_chunks = Column(Integer)

    category = Column(String)

    processing_status = Column(
        String,
        default="PROCESSING"
    )
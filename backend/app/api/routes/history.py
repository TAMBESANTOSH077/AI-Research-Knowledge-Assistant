from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.chat_history_service import get_all_chats

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def history(db: Session = Depends(get_db)):
    return get_all_chats(db)
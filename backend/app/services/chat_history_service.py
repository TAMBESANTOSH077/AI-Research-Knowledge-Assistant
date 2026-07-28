from sqlalchemy.orm import Session

from app.models.chat_history import ChatHistory


def save_chat(db: Session, question: str, answer: str):
    chat = ChatHistory(
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_all_chats(db: Session):
    return db.query(ChatHistory).order_by(ChatHistory.id.desc()).all()
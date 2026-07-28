from datetime import datetime

history = []


def save_chat(question: str, answer: str):
    history.append({
        "question": question,
        "answer": answer,
        "timestamp": datetime.now()
    })


def get_history():
    return history
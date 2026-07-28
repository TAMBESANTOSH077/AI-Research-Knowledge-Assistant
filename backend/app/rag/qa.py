from langchain_groq import ChatGroq

from app.config import settings
from app.rag.hybrid_search import hybrid_search

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=settings.GROQ_API_KEY,
    temperature=0.2,
)


def ask_question(question: str):
    try:
        docs = hybrid_search(question)

        if not docs:
            return {
                "answer": "I couldn't find that information in the uploaded documents.",
                "citations": []
            }

        context = "\n\n".join(doc.page_content for doc in docs)

        citations = [
            {
                "document": doc.metadata.get("document", "Unknown"),
                "page": doc.metadata.get("page", "Unknown"),
                "content": doc.page_content[:200]
            }
            for doc in docs
        ]

        prompt = f"""
You are an AI Research Knowledge Assistant.

Use ONLY the information below.

Context:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)

        return {
            "answer": response.content,
            "citations": citations
        }

    except Exception as e:
        print("QA Error:", e)
        return {
            "answer": f"Error: {str(e)}",
            "citations": []
        }
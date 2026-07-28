from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings
from app.rag.vector_store import vector_store

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GOOGLE_API_KEY,
)

def summarize_document():
    docs = vector_store.similarity_search("", k=10)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Summarize the following document.

Include:
- Overview
- Main Skills
- Experience
- Projects
- Education

Document:

{context}
"""

    response = llm.invoke(prompt)

    return {"summary": response.content}
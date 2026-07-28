from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings
from app.rag.vector_store import vector_store

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0.2,
)


def compare_documents(question: str):
    docs = vector_store.similarity_search(question, k=8)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an AI document comparison assistant.

Compare the documents using ONLY the context below.

Highlight:
- Similarities
- Differences
- Missing information
- Final conclusion

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        "comparison": response.content
    }
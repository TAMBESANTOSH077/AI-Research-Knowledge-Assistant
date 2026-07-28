from app.rag.vector_store import vector_store


def retrieve_with_citations(question: str, k: int = 4):
    docs = vector_store.similarity_search(question, k=k)

    context = "\n\n".join(doc.page_content for doc in docs)

    citations = []

    for doc in docs:
        citations.append({
            "page": doc.metadata.get("page", "Unknown"),
            "content": doc.page_content[:250]
        })

    return context, citations
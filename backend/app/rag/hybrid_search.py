from rank_bm25 import BM25Okapi

from app.rag.vector_store import vector_store


def hybrid_search(query: str, k: int = 4):
    """
    Hybrid Search:
    1. Retrieve relevant documents using Chroma semantic search.
    2. Re-rank them using BM25.
    """

    # Step 1: Semantic Search
    semantic_docs = vector_store.similarity_search(
        query=query,
        k=20
    )

    if not semantic_docs:
        return []

    # Step 2: BM25 Re-ranking
    corpus = [doc.page_content for doc in semantic_docs]
    tokenized_corpus = [text.lower().split() for text in corpus]

    bm25 = BM25Okapi(tokenized_corpus)

    scores = bm25.get_scores(query.lower().split())

    ranked = sorted(
        zip(scores, semantic_docs),
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for _, doc in ranked[:k]]
from app.rag.vector_store import vector_store

query = "What are the candidate's technical skills?"

results = vector_store.similarity_search(query, k=3)

print("\nSearch Results:\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}")
    print("-" * 50)
    print(doc.page_content)
    print("Metadata:", doc.metadata)
    print()
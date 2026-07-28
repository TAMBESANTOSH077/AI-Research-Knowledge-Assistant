from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150,
)


def create_chunks(pages):
    chunks = []

    for page in pages:
        docs = splitter.create_documents(
            [page["text"]],
            metadatas=[{"page": page["page"]}]
        )
        chunks.extend(docs)

    return chunks
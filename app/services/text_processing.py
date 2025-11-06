from langchain_text_splitters.character import RecursiveCharacterTextSplitter

def split_docs(docs, chunk_size=500, chunk_overlap=50):
    """Split large documents into smaller, overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "?", "!", " ", ""],
    )
    return splitter.split_documents(docs)

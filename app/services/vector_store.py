from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings

def build_vector_store(docs):
    """Create a FAISS vector store from a list of documents."""
    embeddings = OpenAIEmbeddings()
    vector = FAISS.from_documents(docs, embeddings)
    return vector

def get_retriever(vector, k=4):
    """Return a retriever for the given vector store."""
    return vector.as_retriever(search_kwargs={"k": k})

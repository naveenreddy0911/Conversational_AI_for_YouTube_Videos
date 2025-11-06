from app.services.transcript_loader import create_docs
from app.services.text_processing import split_docs
from app.services.vector_store import build_vector_store, get_retriever

def get_video_segments(video_id: str, question: str):
    docs = create_docs(video_id)
    split_documents = split_docs(docs)
    vector = build_vector_store(split_documents)

    retriever = get_retriever(vector)
    retrieved = retriever.invoke(question)

    context = ""
    for doc in retrieved:
        context += f"{doc.page_content} (start:{doc.metadata['start']} seconds)\n"
    return context
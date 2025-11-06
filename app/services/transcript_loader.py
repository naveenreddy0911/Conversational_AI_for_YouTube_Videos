from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document

ytt_api = YouTubeTranscriptApi()

def load_transcript(video_id: str):
    """Fetch transcript for a given YouTube video ID."""
    transcript = ytt_api.fetch(video_id)
    return transcript

def create_docs(video_id: str):
    """Convert transcript snippets to LangChain Documents."""
    transcript = load_transcript(video_id)
    return [
        Document(
            page_content=item.text,
            metadata={"start": item.start},
        )
        for item in transcript
    ]

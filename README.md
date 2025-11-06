# Conversational AI for YouTube Videos

A small project that turns YouTube video transcripts into a conversational assistant for generating video-related content (summaries, scripts, question answering, etc.). It uses OpenAI for language processing and a simple backend + frontend layout in this repository.

## Features
- Load and process video transcripts
- Create and query a vector-store of transcript text
- Provide a simple UI for interacting with the conversational assistant

## File structure

Top-level layout:

```
requirements.txt
app/
    main.py               # Backend entrypoint
    prompts/
        prompt_template.py
    services/
        retriever.py
        text_processing.py
        transcript_loader.py
        vector_store.py
ui/
    app.py                # Frontend entrypoint
```

## Environment
Create a `.env` file in the project root (or export the variable in your shell) with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Install requirements
Make a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the backend
From the project root, with your virtualenv activated and `OPENAI_API_KEY` set:

```bash
uvicorn app.main:app --reload
```

## Running the frontend
From the ui folder (cd ui):

```bash
streamlit run main.py
```

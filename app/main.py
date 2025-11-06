from langchain_classic.agents import AgentExecutor,create_react_agent
from app.services.retriever import get_video_segments
from app.prompts.prompt_template import prompt
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
VIDEO_ID = "fkIvmfqX-t0"

class Query(BaseModel):
    query: Annotated[str, Field(description="Your query about the video of fallback knowledge.")]

@tool
def video_query(query:str)->str:
    """
    Retrieve relevant segments from video transcript, along with the start time(if exists).
    """
    result = get_video_segments(VIDEO_ID, query)
    return result

llm=ChatOpenAI()

agent=create_react_agent(
    llm=llm,
    tools=[video_query],
    prompt=prompt
)

agent_executor=AgentExecutor(
    agent=agent,
    tools=[video_query],
    verbose=True,
    handle_parsing_errors=True
)

@app.get("/")
def home():
    return {"message":"Youtube Video Helper"}

@app.post("/query")
def handle_query(data: Query):
    result = agent_executor.invoke({"input": data.query})
    return {"result": result}
# app/climate_routes.py

from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from climate_agent.qa import ask_question
from climate_agent.vector_store import ingest_and_process
from climate_agent.summary import generate_summary_from_store

router = APIRouter()

# Model for /ask endpoint
class Question(BaseModel):
    query: str

@router.post("/ask")
def ask(question: Question):
    response = ask_question(question.query)
    if response:
        return response
    raise HTTPException(status_code=400, detail="Error processing question")

@router.post("/ingest")
def ingest_route(payload: dict = Body(...)):
    urls = payload.get("urls", [])
    if not urls:
        return {"error": "No URLs provided."}
    result = ingest_and_process(urls)
    return result

@router.get("/summary")
def get_summary():
    try:
        summary = generate_summary_from_store()
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

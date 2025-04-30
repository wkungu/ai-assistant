from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from app.core.prompt_engine import generate_ai_response
from app.services.history_store import get_history

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Business Advisor AI API!"}

@router.get("/history", tags=["History"])
async def fetch_query_history():
    return {"history": get_history()}

@router.post("/query", tags=["Query"])
async def query_ai(payload: QueryRequest, request: Request):
    if not payload.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    try:
        response = await generate_ai_response(payload.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from pydantic import BaseModel
from typing import List
from datetime import datetime

class QueryResponse(BaseModel):
    response: str

class HistoryItem(BaseModel):
    question: str
    response: str
    timestamp: datetime

class HistoryResponse(BaseModel):
    history: List[HistoryItem]

class RootResponse(BaseModel):
    message: str

from pydantic import BaseModel
from typing import Optional, List

class QueryRequest(BaseModel):
    query: str
    strategy: str = "hybrid_rerank"
    filters: Optional[dict] = None

class DocumentResponse(BaseModel):
    id: str
    filename: str
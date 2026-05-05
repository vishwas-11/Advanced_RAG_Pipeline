from fastapi import APIRouter
from app.models.schemas import QueryRequest
from app.services.rag_chain import generate_answer

router = APIRouter()

@router.post("/")
def query(payload: QueryRequest):
    answer = generate_answer("dummy context", payload.query)
    return {"answer": answer}

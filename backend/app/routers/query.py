from fastapi import APIRouter
from app.models.schemas import QueryRequest
from app.services.rag_chain import answer_from_documents

router = APIRouter()

@router.post("/")
def query(payload: QueryRequest):
    answer = answer_from_documents(payload.query)
    return {"answer": answer}

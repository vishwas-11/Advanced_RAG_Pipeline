from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def evaluate():
    return {"status": "evaluation started"}
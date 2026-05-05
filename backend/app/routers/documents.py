from fastapi import APIRouter, File, UploadFile
from app.services.ingestion import load_document

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()

    with open(file.filename, "wb") as f:
        f.write(content)

    docs = load_document(file.filename)

    return {"message": "uploaded", "chunks": len(docs)}

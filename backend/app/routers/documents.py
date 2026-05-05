from fastapi import APIRouter, Depends, File, UploadFile
from pathlib import Path

from app.core.auth import get_current_user
from app.services.ingestion import ingest_document

router = APIRouter()
UPLOAD_DIR = Path("./uploads")


@router.post("/upload")
async def upload(file: UploadFile = File(...), user=Depends(get_current_user)):
    content = await file.read()
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(content)

    docs = ingest_document(str(file_path))

    return {
        "message": "uploaded",
        "user_id": user["user_id"],
        "chunks": len(docs),
    }

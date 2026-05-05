from fastapi import FastAPI
from app.routers import documents, query, evaluation

app = FastAPI(title="Advanced RAG Platform")

app.include_router(documents.router, prefix="/api/documents")
app.include_router(query.router, prefix="/api/query")
app.include_router(evaluation.router, prefix="/api/evaluate")

@app.get("/api/health")
def health():
    return {
        "message": "Advanced RAG Platform is healthy",
        "status": "ok"
    }


@app.get("/")
def root():
    return {
        "message": "Advanced RAG Platform is up and running",
        "status": "ok"
    }

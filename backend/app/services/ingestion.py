from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredMarkdownLoader,
)
from datetime import datetime
from pathlib import Path

from app.services.chunking_strategies import recursive_chunks
from app.services.vector_store import clear_vector_collection, get_vector_store

UPLOAD_DIR = Path("./uploads")


def load_document(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = UnstructuredWordDocumentLoader(file_path)
    else:
        loader = UnstructuredMarkdownLoader(file_path)

    docs = loader.load()

    for doc in docs:
        doc.metadata["upload_date"] = str(datetime.utcnow())

    return docs


def ingest_document(file_path: str):
    docs = load_document(file_path)
    chunks = recursive_chunks(docs)

    for chunk in chunks:
        chunk.metadata["source_file"] = Path(file_path).name
        chunk.metadata["upload_date"] = str(datetime.utcnow())

    clear_vector_collection()
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    return chunks

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MONGO_URI = os.getenv("MONGO_URI")

MONGODB_VECTOR_DB = os.getenv("MONGODB_VECTOR_DB", "rag_db")
MONGODB_VECTOR_COLLECTION = os.getenv("MONGODB_VECTOR_COLLECTION", "document_chunks")
MONGODB_VECTOR_INDEX = os.getenv("MONGODB_VECTOR_INDEX", "vector_index")

OPENAI_CHAT_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-large"

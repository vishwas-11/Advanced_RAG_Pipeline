from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["rag_db"]

documents_collection = db["documents"]
chunks_collection = db["chunks"]
queries_collection = db["queries"]
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MONGO_URI = os.getenv("MONGO_URI")

CHROMA_DIR = "./chroma_db"

EMBEDDING_MODEL = "text-embedding-3-small"
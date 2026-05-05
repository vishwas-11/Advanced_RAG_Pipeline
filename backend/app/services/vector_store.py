from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch

from app.config import (
    EMBEDDING_MODEL,
    MONGO_URI,
    MONGODB_VECTOR_COLLECTION,
    MONGODB_VECTOR_DB,
    MONGODB_VECTOR_INDEX,
    OPENAI_API_KEY,
)


def get_embeddings():
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to .env or the environment before using embeddings."
        )

    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        api_key=OPENAI_API_KEY,
    )


def get_vector_store():
    return MongoDBAtlasVectorSearch.from_connection_string(
        connection_string=MONGO_URI,
        namespace=f"{MONGODB_VECTOR_DB}.{MONGODB_VECTOR_COLLECTION}",
        embedding=get_embeddings(),
        index_name=MONGODB_VECTOR_INDEX,
        text_key="page_content",
        embedding_key="embedding",
        relevance_score_fn="cosine",
    )


def clear_vector_collection():
    client = MongoClient(MONGO_URI)
    collection = client[MONGODB_VECTOR_DB][MONGODB_VECTOR_COLLECTION]
    collection.delete_many({})

from langchain.retrievers import EnsembleRetriever
from rank_bm25 import BM25Okapi


def hybrid_retriever(vector_retriever, docs):
    corpus = [doc.page_content for doc in docs]
    bm25 = BM25Okapi([doc.split() for doc in corpus])

    return EnsembleRetriever(
        retrievers=[vector_retriever],
        weights=[0.7, 0.3]
    )
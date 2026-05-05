from functools import lru_cache
from sentence_transformers import CrossEncoder

@lru_cache(maxsize=1)
def get_model():
    return CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    pairs = [(query, d.page_content) for d in docs]
    scores = get_model().predict(pairs)

    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked[:5]]

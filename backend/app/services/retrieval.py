from app.services.vector_store import get_vector_store


def retrieve_context(query: str, k: int = 4):
    vector_store = get_vector_store()
    docs = vector_store.similarity_search(query, k=k)

    context_parts = []
    for doc in docs:
        source_file = doc.metadata.get("source_file", "uploaded document")
        page = doc.metadata.get("page", "")
        page_info = f"page {page}" if page != "" else "page unknown"
        context_parts.append(f"[{source_file}, {page_info}] {doc.page_content}")

    return "\n\n".join(context_parts), docs

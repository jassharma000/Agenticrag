from app.retrieval.vectorstore import get_vectorstore
from app.retrieval.bm25_retrieval import bm25_search



def hybrid_search(query: str) -> str:
    """
    Perform a hybrid search using both vector and keyword-based retrieval methods.
    
    Args:
        query (str): The search query input by the user.
        """
    
    vector_store = get_vectorstore()

    vector_docs = vector_store.similarity_search(query, k=5)

    bm25_docs = bm25_search(query)

    combined_docs = vector_docs + bm25_docs

    unique_docs = []

    seen = set()

    for doc in combined_docs:

        if doc.page_content not in seen:
            unique_docs.append(doc)
            seen.add(doc.page_content)

    return unique_docs
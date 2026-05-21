import json
import os

from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever

chunks_path = "data/processed/chunks.json"

def load_chunks():
    """ load locally stored chunks from json
    and reconstruct them into Document objects
    """
    with open(chunks_path, "r") as f:
        chunks = json.load(f)

    documents = []

    for chunk in chunks:

        doc = Document(
            page_content=chunk["page_content"],
            metadata=chunk["metadata"]
        )

        documents.append(doc)

    return documents

# load all documents

documents = load_chunks()

bm25_retriever = BM25Retriever.from_documents(documents)

bm25_retriever.k = 5

def bm25_search(query, source: str = None):

    """ perform a bm25 search on the locally stored chunks
    using the query provided by the user
    """

    results = bm25_retriever.invoke(query)

    if source:
        filtered_results = []

        for doc in results:

            if doc.metadata.get("source") == source:
                filtered_results.append(doc)
        return filtered_results
    return results

print(  bm25_search("Rajasthan tenancy rules when did this rule came out"))
from langchain_core.tools import tool

from app.retrieval.hybrid_retriever import hybrid_search


@tool
def retrieve_documents(query:str )-> str:

    """
    Retrieve relevant documents from the knowledge base.
    Useful for answering domain-specific questions.
    """

    docs =  hybrid_search(query)

    formatted_docs = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return formatted_docs
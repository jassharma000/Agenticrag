from langchain_pinecone import PineconeVectorStore

from app.ingestion.embeddings import get_embeddings

embeddings = get_embeddings()

def get_vectorstore() :

    vectorstore = PineconeVectorStore(
        index_name = "agenticrag",
        embedding = embeddings
    )

    return vectorstore


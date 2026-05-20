from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunking import split_documents
from langchain_community.document_loaders import PyPDFLoader
from app.retrieval.vectorstore import get_vectorstore
import os
import json


chunks_path = "data/processed/chunks.json"

#saving the chunks locally as json for bm25 retrieval
def save_chunks_locally(new_chunks):

    existing_chunks = []

    if os.path.exists(chunks_path):

        with open(chunks_path, "r") as f:
            existing_chunks = json.load(f)

    existing_chunks.extend(new_chunks)

    with open(chunks_path, "w") as f:
        json.dump(existing_chunks, f, indent=4)

def load_pdf(pdf_file):

    loader = PyPDFLoader(pdf_file)

    documents = loader.load()

    return documents

def ingest_pdf(pdf_dir):

    vectorstore = get_vectorstore()

    all_chunks = []

    for filename in os.listdir(pdf_dir):

        if not filename.endswith(".pdf"):
            continue

        file_path = os.path.join(pdf_dir, filename)

        print(f"Ingesting: {filename}")

        documents = load_pdf(file_path)

        chunks = split_documents(documents)

        for chunk in chunks:

            chunk.metadata["source"] = filename

            all_chunks.append({
                "page_content": chunk.page_content,
                "metadata": chunk.metadata
            })

        vectorstore.add_documents(chunks)

    save_chunks_locally(all_chunks)

    print("All pdfs ingested successfully")    

print("Starting PDF ingestion...")
ingest_pdf("data/raw_pdfs")
print("PDF ingestion completed.")
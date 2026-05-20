from langchain_community.document_loaders import PyPDFLoader
import os

all_documents = []

def load_pdf(pdf_path):

    files = os.listdir(pdf_path)
    for file in files:
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_path, file))
            documents = loader.load()
            all_documents.extend(documents)
            
    return all_documents


    
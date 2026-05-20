from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    print("Splitting documents into chunks...",len(documents))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,

    )

    chunks = splitter.split_documents(documents)

    print("Chunks created:", len(chunks))

    return chunks


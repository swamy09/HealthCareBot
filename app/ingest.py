from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

from config import (
    embedding_model,
    PINECONE_API_KEY,
    PINECONE_INDEX,
)


#we have loaded the document
def loadpdf():
    loader = PyPDFLoader("./data/Medical_book.pdf")
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")
    print(documents[10].page_content[:300])

    return documents

# we are creating the pinecone index from code.
def create_pinecone_index():

# 3. Initialize the Pinecone client
    pc = Pinecone(api_key=PINECONE_API_KEY)

    print("🎉 Pinecone initialized successfully!")

    index_name = PINECONE_INDEX

    if not pc.has_index(index_name):
        pc.create_index(
        name =index_name,
        dimension=1024,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    
    return index_name

# now we will embedd the model.

def ingest_vector_pinecone(index_name,documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    print(f"Total chunks: {len(chunks)}")

# here we have created an vectors and stored the pineconde as index
    docsearch = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embedding_model,
        index_name=index_name
    )

# its sample to use the existing index, note - we can directly assign the creation to one object/var and use here we are doing it to understand.

    # docsearch = PineconeVectorStore.from_existing_index(
    #     index_name=index_name,
    #     embedding=embedding_model
    # )
# to add the new documents to same pinecone index
    # docsearch.add_documents(documents=[])


    print("Documents uploaded successfully!")

    return docsearch



if __name__ == "__main__":
    documents = loadpdf()
    index_name = create_pinecone_index()
    docsearch = ingest_vector_pinecone(index_name, documents)









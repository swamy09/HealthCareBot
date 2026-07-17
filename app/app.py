from flask import Flask, render_template, jsonify, request
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

#here we are importing from the config file
from config import (
    embedding_model,
    PINECONE_API_KEY,
    PINECONE_INDEX,
    answer_llm
)

#to run legacy
from rag_chain import create_rag_chain

#where we are importing the Rag chain from rag file
#from workflows.agentic_rag import AgenticRAG

#flash initialisation 
app = Flask(__name__)

#we are accessing the pineconeindex which we have built
docsearch = PineconeVectorStore.from_existing_index(
        index_name=PINECONE_INDEX,
        embedding=embedding_model
    )

#create the Rag chain
#agentic_rag = AgenticRAG(docsearch)

#to run legacy
rag_chain = create_rag_chain(docsearch)


#this is for rendering the HTML file
@app.route("/")
def index():
    return render_template('chat.html')

# THis is the place we are getting the question from customer and sending to llm model.
@app.route("/get", methods = ["GET","POST"])
def chat():
    msg = request.form["msg"]

    print("User:", msg)
    print("Calling RAG chain...")

    # to run legacy
    response = rag_chain.invoke(msg)

    #response = agentic_rag.invoke(msg)

    print("RAG chain finished.")
    print("Bot:", response)
 

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug=False, use_reloader=False)
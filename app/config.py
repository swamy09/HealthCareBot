import os
from dotenv import load_dotenv
from langchain_nvidia import NVIDIAEmbeddings, ChatNVIDIA

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = "health-care-bot"

embedding_model = NVIDIAEmbeddings(
    model="nvidia/nv-embedqa-e5-v5"
)

answer_llm = ChatNVIDIA(
    model="deepseek-ai/deepseek-v4-flash",
    temperature=0.3
)

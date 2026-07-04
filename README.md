# HealthCareBot

# 🏥 Healthcare RAG Chatbot

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot built using **Python, Flask, LangChain, NVIDIA AI Endpoints, and Pinecone Vector Database**.

The chatbot allows users to ask healthcare-related questions and receives context-aware answers by retrieving information from a medical knowledge base instead of relying only on an LLM.

---

# 📌 Features

- 💬 Interactive healthcare chatbot
- 📄 PDF document ingestion
- ✂️ Intelligent text chunking
- 🧠 Embedding generation
- 📚 Pinecone Vector Database
- 🔍 Semantic search and retrieval
- 🤖 LLM-powered response generation
- 📊 LangSmith tracing and monitoring
- 🐳 Docker containerization
- ☁️ Azure App Service deployment
- 🚀 CI/CD using GitHub Actions

---

# Project Architecture

```

User
│
▼
Flask Web App
│
▼
LangChain RAG Pipeline
│
├──────────────┐
│              │
▼              ▼
Retriever      NVIDIA LLM
│              │
▼              │
Pinecone Vector DB
│
▼
Medical PDF Knowledge Base

```

---

# Tech Stack

## Backend

- Python 3.11
- Flask

## AI Framework

- LangChain

## Large Language Model

- NVIDIA AI Endpoints

Examples:

- DeepSeek V4 Flash
- Kimi K2
- Llama 3.3 70B

(Models can easily be swapped.)

## Embedding Model

- NVIDIA Embedding Model

## Vector Database

- Pinecone

## Monitoring

- LangSmith

## Deployment

- Docker
- Azure Container Registry (ACR)
- Azure App Service

## CI/CD

- GitHub Actions

---

# Folder Structure

```

HealthCareBot/
│
├── app/
│ ├── app.py
│ ├── config.py
│ ├── ingest.py
│ ├── rag_chain.py
│ ├── templates/
│ └── static/
│
├── data/
│ └── Medical_book.pdf
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md

```

---

# Project Workflow

The project follows a standard RAG pipeline.

```

Medical PDF
│
▼
Load PDF
│
▼
Split into Chunks
│
▼
Generate Embeddings
│
▼
Store in Pinecone
│
▼
User asks Question
│
▼
Retrieve Relevant Chunks
│
▼
Combine Question + Context
│
▼
LLM Generates Answer
│
▼
Return Response

```

---

# How RAG Works

Instead of asking the LLM directly,

the chatbot first searches the vector database for the most relevant pieces of information.

These retrieved chunks are then sent to the language model as context.

This greatly improves:

- Accuracy
- Hallucination reduction
- Domain-specific knowledge
- Response quality

---

# Application Flow

```

Browser

↓

Flask Route (/get)

↓

rag_chain.invoke()

↓

Retriever (Pinecone)

↓

Relevant Documents

↓

Prompt Template

↓

NVIDIA LLM

↓

Generated Answer

↓

Browser

```

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Flask | Web framework |
| LangChain | RAG orchestration |
| Pinecone | Vector database |
| NVIDIA AI Endpoints | LLM inference |
| NVIDIA Embeddings | Text embeddings |
| LangSmith | Monitoring & tracing |
| Docker | Containerization |
| Azure App Service | Hosting |
| Azure Container Registry | Docker image registry |
| GitHub Actions | CI/CD |

---

# LangSmith Monitoring

The application is integrated with LangSmith for tracing.

LangSmith provides:

- Complete RAG execution traces
- Retriever latency
- LLM latency
- Token usage
- Prompt inspection
- Response inspection
- Debugging
- Performance monitoring

Example Trace

```

User Question

↓

Retriever

↓

Retrieved Chunks

↓

Prompt

↓

LLM

↓

Response

```

---

# Docker

The application is containerized using Docker.

Docker ensures that the application runs consistently across:

- Local machine
- Testing environments
- Production

### Docker Build

```

docker build -t healthcare-rag .

```

### Docker Run

```

docker run -p 8080:8080 healthcare-rag

```

---

# Azure Deployment

The application is deployed using:

- Azure Container Registry (ACR)
- Azure App Service (Linux Container)

Deployment Flow

```

Git Push

↓

GitHub Actions

↓

Docker Build

↓

Azure Container Registry

↓

Azure App Service

↓

Live Application

```

---

# GitHub Actions CI/CD

Every push to the **main** branch automatically:

1. Checks out the repository
2. Logs into Azure
3. Builds the Docker image
4. Pushes the image to Azure Container Registry
5. Updates Azure App Service
6. Restarts the application

No manual deployment is required.

---

# Environment Variables

The project requires several environment variables.

Examples include:

```

PINECONE_API_KEY

NVIDIA_API_KEY

LANGSMITH_API_KEY

LANGSMITH_PROJECT

```

> **Important:** Never commit API keys, secrets, passwords, or credentials to the repository.

---

# Getting Started

## Clone Repository

```

git clone <repository-url>

cd HealthCareBot

```

---

## Create Virtual Environment

Windows

```

python -m venv .venv

.venv\Scripts\activate

```

Linux / macOS

```

python3 -m venv .venv

source .venv/bin/activate

```

---

## Install Dependencies

```

pip install -r requirements.txt

```

---

## Configure Environment Variables

Create a `.env` file in the project root.

Add your own API keys and configuration values.

> Never commit the `.env` file.

---

## Ingest Documents

Before running the chatbot, populate the vector database.

```

python app/ingest.py

```

This will:

- Load the PDF
- Split it into chunks
- Generate embeddings
- Upload vectors to Pinecone

---

## Run Application

```

python app/app.py

```

Open:

```

http://localhost:8080

```

---

# Future Improvements

- Conversation memory
- Multiple PDF support
- User authentication
- Chat history
- Source citations
- Streaming responses
- Hybrid search
- Reranking
- Feedback collection
- Evaluation pipeline
- Multi-agent workflow
- Medical disclaimer integration

---

# Learning Outcomes

This project demonstrates practical knowledge of:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embeddings
- LangChain
- Prompt Engineering
- LLM Integration
- Flask Development
- Docker
- Azure Cloud
- GitHub Actions
- CI/CD Pipelines
- LangSmith Monitoring

---

# Disclaimer

This chatbot is intended for educational and demonstration purposes only.

It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical concerns.

---

# License

This project is licensed under the MIT License.

---

# Author

Developed as a personal learning project to explore modern AI application development using Retrieval-Augmented Generation (RAG), LangChain, Vector Databases, Docker, Azure Cloud, and CI/CD best practices.
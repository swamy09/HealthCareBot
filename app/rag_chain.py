from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from config import (
    answer_llm
)


def create_rag_chain(docsearch):
    retriever = docsearch.as_retriever(
        search_type="similarity", search_kwargs={"k": 2}
    )

     # RAG Prompt Template
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful healthcare assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, reply exactly:
"I don't know."

Keep your answers concise and accurate.

Context:
{context}
""",
        ),
        (
            "human",
            "{question}",
        ),
    ]
)

    # Format retrieved docs
    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    # Rag chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | answer_llm
        | StrOutputParser()
    )

    return rag_chain
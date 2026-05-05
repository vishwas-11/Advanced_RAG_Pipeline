from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

from app.config import OPENAI_API_KEY, OPENAI_CHAT_MODEL
from app.services.retrieval import retrieve_context

prompt = ChatPromptTemplate.from_template("""
You are a document question-answering assistant.
Answer only from the provided context.
If the answer is not present in the context, say exactly:
The uploaded document does not contain enough information to answer that.

Context:
{context}

Question: {question}
""")

def get_llm():
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to .env or the environment before calling /api/query."
        )
    return ChatOpenAI(
        model=OPENAI_CHAT_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0,
    )

def generate_answer(context, question):
    chain = prompt | get_llm()
    return chain.invoke({
        "context": context,
        "question": question
    })


def answer_from_documents(question: str):
    context, docs = retrieve_context(question)

    if not docs:
        return "The uploaded document does not contain enough information to answer that."

    answer = generate_answer(context, question)
    return answer.content if hasattr(answer, "content") else str(answer)

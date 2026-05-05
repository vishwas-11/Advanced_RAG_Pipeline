from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

from app.config import OPENAI_API_KEY

prompt = ChatPromptTemplate.from_template("""
Answer based only on context:
{context}

Question: {question}
""")

def get_llm():
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to .env or the environment before calling /api/query."
        )
    return ChatOpenAI(api_key=OPENAI_API_KEY)

def generate_answer(context, question):
    chain = prompt | get_llm()
    return chain.invoke({
        "context": context,
        "question": question
    })

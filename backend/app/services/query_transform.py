from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.config import OPENAI_API_KEY, OPENAI_CHAT_MODEL

def get_llm():
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to .env or the environment before using query transforms."
        )
    return ChatOpenAI(
        model=OPENAI_CHAT_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0,
    )

def multi_query(query):
    prompt = ChatPromptTemplate.from_template(
        "Generate 3 variations of: {query}"
    )
    chain = prompt | get_llm()
    return chain.invoke({"query": query})

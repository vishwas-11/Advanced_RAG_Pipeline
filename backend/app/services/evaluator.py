from langchain_openai import ChatOpenAI

from app.config import OPENAI_API_KEY, OPENAI_CHAT_MODEL

def get_llm():
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to .env or the environment before running evaluation."
        )
    return ChatOpenAI(
        model=OPENAI_CHAT_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0,
    )

def evaluate_faithfulness(answer, context):
    prompt = f"Is this answer supported by context?\nAnswer:{answer}\nContext:{context}"
    return get_llm().invoke(prompt)

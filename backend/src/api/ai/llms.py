import os
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


LLM_BASE_URL = os.environ.get("LLM_BASE_URL") or None
LLM_MODEL_NAME = os.environ.get("LLM_MODEL_NAME") or "gpt-4o-mini"
LLM_API_KEY = os.environ.get("LLM_API_KEY") or None
IS_PROD = os.environ.get("IS_PROD") or None

chat_model_obj = {
    'base_url': LLM_BASE_URL,
    'model': LLM_MODEL_NAME
}
if IS_PROD == "True":
    chat_model_obj['api_key'] = LLM_API_KEY
    if not LLM_API_KEY:
        raise NotImplementedError("`LLM_API_KEY` is not defined.")
    

def get_ollama_llm():
    return ChatOllama(**chat_model_obj) if IS_PROD == "True" else ChatOpenAI(**chat_model_obj)


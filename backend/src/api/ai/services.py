from api.ai.llms import get_ollama_llm
from api.ai.schemas import EmailMessageSchema
from langchain.messages import HumanMessage, AIMessage, SystemMessage


def generate_email_message(query: str):
    llm_base = get_ollama_llm()
    llm = llm_base.with_structured_output(EmailMessageSchema)

    messages = [
        SystemMessage(content="You are a helpful assistant for research and composing plaintext emails. Do not use markdown in your response only plaintext."),
        HumanMessage(content=f"{query}. Do not use markdown in your response only plaintext")
    ]
    return llm.invoke(messages)
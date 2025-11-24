from langchain.messages import SystemMessage, HumanMessage

from api.ai.llms import get_ollama_llm
from api.ai.tools import send_email_tool, get_unread_mails_tool


EMAIL_TOOLS = {
    "send_email_tool": send_email_tool,
    "get_unread_mails_tool": get_unread_mails_tool
}

def email_assitance(query: str):
    llm_base = get_ollama_llm()
    llm = llm_base.bind_tools(list(EMAIL_TOOLS.values()))
    messages = [
        SystemMessage(content="You are a helpful assistant for research and composing plaintext emails. Do not use markdown in your response only plaintext."),
        HumanMessage(content=f"{query}. Do not use markdown in your response only plaintext")
    ]
    response = llm.invoke(messages)
    messages.append(response)
    # print(f"Got AI response - {response}")
    if hasattr(response, "tool_calls") and response.tool_calls:
        # print(f"tool_calls in attrs")
        for tool_call in response.tool_calls:
            tool_name = tool_call.get("name")
            tool_args = tool_call.get("args")
            tool_func = EMAIL_TOOLS.get(tool_name)
            if not tool_func:
                continue
            # print(f"Calling tool - {tool_name} with args - {tool_args}")
            tool_result = tool_func.invoke(tool_args)
            # print(f"\n\n\n tool_result - {tool_result}\n\n")
            messages.append(tool_result)
        # print(f"Called all tools now generating full response.")
        final_response = llm.invoke(messages)
        return final_response
    
    return response
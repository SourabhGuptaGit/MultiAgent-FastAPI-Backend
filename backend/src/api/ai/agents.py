from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from api.ai.llms import get_ollama_llm
from api.ai.tools import send_email_tool, get_unread_mails_tool, research_email


agentic_tools = [send_email_tool, get_unread_mails_tool]

def exec_email_agent(_exec: bool = False, query: str = ""):
    model = get_ollama_llm()
    agent = create_react_agent(
        model=model,
        tools=agentic_tools,
        prompt="You are a helpful assistant for research and composing plaintext emails. Do not use markdown in your response only plaintext.",
        name="email_agent"
    )
    if _exec:
        response = agent.invoke({
            "message": [{
                "role": "user", "content": query
            }]
        })
        return response
    return agent

def exec_research_agent(_exec: bool = False, query: str = ""):
    model = get_ollama_llm()
    agent = create_react_agent(
        model=model,
        tools=[research_email],
        prompt="You are a helpful research assistant for preparing emails data.",
        name="research_agent"
    )
    if _exec:
        response = agent.invoke({
            "message": [{
                "role": "user", "content": query
            }]
        })
        return response
    return agent

def exec_supervisor(_exec: bool = False, query: str = ""):
    llm = get_ollama_llm()
    email_agent = exec_email_agent()
    research_agent = exec_research_agent()
    
    super_v = create_supervisor(
        agents=[email_agent, research_agent],
        model=llm,
        prompt=(
            "You manage a  research assistant and a"
            "email inbox manager assistant, assign work to them."
        )
    ).compile()
    
    if _exec:
        response = super_v.invoke({
            "message": [{
                "role": "user", "content": query
            }]
        })
        return response
    return super_v

# from api.ai.agents import exec_supervisor, exec_email_agent, exec_research_agent
# research_agent = exec_research_agent()
# email_agent = exec_email_agent()
# super_agent = exec_supervisor()
import os

# Step 1: API key check
print("OPENAI KEY:", os.environ.get("OPENAI_API_KEY"))

# Step 2: LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly"



def get_response_from_ai_agent(llm_id, query, allow_search, provider):

    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Invalid provider")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # ✅ query is already a list of messages
    state = {
        "messages": query
    }

    response = agent.invoke(state)

    messages = response.get("messages", [])

    ai_messages = [
        msg.content for msg in messages if isinstance(msg, AIMessage)
    ]

    return ai_messages[-1] if ai_messages else ""


# -------- RUN ----------
answer = get_response_from_ai_agent(
    llm_id="llama-3.3-70b-versatile",
    query="Tell me about the trends in crypto markets",
    allow_search=True,
    provider="Groq"
)

print(answer)

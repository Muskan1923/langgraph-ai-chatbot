# langgraph-ai-chatbot

# 🤖 AI Chatbot Agent (LangGraph + Groq + OpenAI)

This project is a full-stack **AI Chatbot Agent** built using **LangGraph**, **LangChain**, **FastAPI**, and **Streamlit**.  
It supports multiple LLM providers like **Groq** and **OpenAI**, with optional **web search** powered by **Tavily**.

## 🚀 Features

- 🔁 Multi-model support (Groq & OpenAI)
- 🌐 Optional web search using Tavily
- ⚙️ Backend API built with FastAPI
- 🖥️ Interactive frontend using Streamlit
- 🔑 Secure API key handling via environment variables
- 🧠 LangGraph ReAct-style AI agent

## 🧩 Tech Stack

- Python  
- LangChain  
- LangGraph  
- Groq API  
- OpenAI API  
- Tavily Search API  
- FastAPI  
- Streamlit  
- Uvicorn  

## 📁 Project Structure
Ai agent chatbot/
│
├── ai_agent.py # Core AI agent logic

├── backend.py # FastAPI backend

├── frontend.py # Streamlit frontend UI

├── .env # Environment variables (not committed)

├── requirements.txt # Dependencies

└── README.md

## 🔐 Environment Variables
Set the following API keys in your system:

```bash
setx OPENAI_API_KEY "your_openai_key"
setx GROQ_API_KEY "your_groq_key"
setx TAVILY_API_KEY "your_tavily_key"

▶️ Run the Application
1️⃣ Start Backend (FastAPI)
python backend.py

Backend runs at:
http://127.0.0.1:9999

Swagger Docs:
http://127.0.0.1:9999/docs

2️⃣ Start Frontend (Streamlit)
streamlit run frontend.py

Example Backend Request
{
  "model_name": "llama-3.3-70b-versatile",
  "model_providers": "Groq",
  "system_prompt": "Act as a helpful AI assistant",
  "messages": ["What is the capital of Australia?"],
  "allow_search": false
}

##💡 How It Works
1.User enters query in Streamlit UI
2.Frontend sends request to FastAPI backend
3.Backend calls ai_agent.py
4.LangGraph agent decides whether to use web search
5.LLM generates final response
6.Answer is displayed in UI

##👩‍💻 Author
Arpita Bagdawat
B.Tech (AI & Data Science)
Aspiring Data Scientist & AI Engineer


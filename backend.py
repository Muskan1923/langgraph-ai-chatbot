#step1: setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_providers: str#step1: setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_providers: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

#step2: setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192","mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app=FastAPI(title="LangGraph AI Agent")

from fastapi import HTTPException

from fastapi import HTTPException

@app.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        if request.model_name not in ALLOWED_MODEL_NAMES:
            raise HTTPException(status_code=400, detail="Invalid model name")

        response = get_response_from_ai_agent(
            request.model_name,
            request.messages,
            request.allow_search,
            request.model_providers
        )

        return response

    except HTTPException as e:
        # re-raise FastAPI errors as-is
        raise e

    except Exception as e:
        print("UNEXPECTED ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


#step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
    system_prompt: str
    messages: List[str]
    allow_search: bool

#step2: setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192","mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app=FastAPI(title="LangGraph AI Agent")

from fastapi import HTTPException

from fastapi import HTTPException

@app.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        if request.model_name not in ALLOWED_MODEL_NAMES:
            raise HTTPException(status_code=400, detail="Invalid model name")

        response = get_response_from_ai_agent(
            request.model_name,
            request.messages,
            request.allow_search,
            request.model_providers
        )

        return response

    except HTTPException as e:
        # re-raise FastAPI errors as-is
        raise e

    except Exception as e:
        print("UNEXPECTED ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


#step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
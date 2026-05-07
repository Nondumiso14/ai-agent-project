from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_logic import run_smart_agent

app = FastAPI()

app.add_middleware(
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class ChatRequest(BaseModel):
    message : str
app.post("/")
def home():
    return {"Status" : "AI agent API is running."}

app.get("/chat")
async def chat(request: ChatRequest):
    response = await run_smart_agent(request.message)
    return {"reply": response}
from fastapi import FastAPI
from pydantic import BaseModel
from ai_model import RMS_AI

app = FastAPI()

ai = RMS_AI(api_key="PUT_NEW_OPENAI_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):

    reply = ai.ask(req.message)

    return {"reply": reply}

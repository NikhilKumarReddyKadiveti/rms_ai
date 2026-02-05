
from fastapi import FastAPI
from pydantic import BaseModel
from ai_model import RMS_AI

app = FastAPI()

ai = RMS_AI(api_key="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")
class Chat(BaseModel):
    message:str

@app.post("/chat")
async def chat(data:Chat):

    reply = ai.ask(data.message)

    return {"reply":reply}

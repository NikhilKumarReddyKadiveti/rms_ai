from openai import OpenAI
from prompts import SYSTEM_PROMPT
from memory import ChatMemory

class RMS_AI:

    def __init__(self, api_key):

        self.client = OpenAI(api_key=api_key)
        self.memory = ChatMemory()

    def ask(self, message):

        msgs = [
            {"role":"system","content":SYSTEM_PROMPT}
        ]

        msgs += self.memory.get()

        msgs.append({"role":"user","content":message})

        res = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=msgs
        )

        reply = res.choices[0].message.content

        self.memory.add_user(message)
        self.memory.add_ai(reply)

        return reply

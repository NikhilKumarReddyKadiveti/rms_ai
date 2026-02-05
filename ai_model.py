from openai import OpenAI
from prompts import SYSTEM_PROMPT
from memory import ChatMemory

class RMS_AI:

    def __init__(self, api_key):

        self.client = OpenAI(api_key=api_key)
        self.memory = ChatMemory()

    def build_messages(self, user_message):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages += self.memory.get_messages()

        messages.append({
            "role": "user",
            "content": user_message
        })

        return messages

    def ask(self, user_message):

        messages = self.build_messages(user_message)

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages
        )

        reply = response.choices[0].message.content

        self.memory.add_user(user_message)
        self.memory.add_ai(reply)

        return reply

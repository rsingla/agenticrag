from mistralai import Mistral

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-tiny"

client = Mistral(api_key=api_key)

messages = [
    {
        "role": "user",
        "content": "Who is the most renowned French painter?"
    }
]

response = client.chat.complete(
    model=model,
    messages=messages,
    max_tokens=100,
    temperature=0.5,
    top_p=0.9
)

print(response)
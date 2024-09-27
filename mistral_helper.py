from mistralai import Mistral

import os
from dotenv import load_dotenv, find_dotenv    

load_dotenv(find_dotenv()) 

# Set your Mistral API Key as an environment variable.
# You can find your API key on the Mistral website.
mistral_api_key = os.getenv("MISTRAL_API_KEY")

def mistral_ai(user_message, model="mistral-large-latest", is_json=False):
    # Initialize the Mistral client
    client = Mistral(api_key=mistral_api_key)

    print(user_message)

    # Send a chat request to the model
    if is_json:
        chat_response = client.chat.complete(
            model=model,  # Use the latest Mistral large language model
            messages=[
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            response_format={ "type": "json_object" }
        )
    else:    
        chat_response = client.chat.complete(
            model=model,  # Use the latest Mistral large language model
            messages=[
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
        )

    return chat_response.choices[0].message.content
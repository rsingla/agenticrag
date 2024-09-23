import os
import requests
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

def print_json_keys(json_data, indent=""):
  """
  Recursively prints all keys in a JSON object.

  Args:
    json_data: The JSON data to print keys from (can be a dict, list, or primitive value).
    indent: The indentation string to use for nested objects.
  """
  if isinstance(json_data, dict):
    for key, value in json_data.items():
      print(f"{indent}- {key}")
      print_json_keys(value, indent + "  ")
  elif isinstance(json_data, list):
    for item in json_data:
      print_json_keys(item, indent + "  ")  # No key to print for list items


# Set your Mistral API Key as an environment variable.
# You can find your API key on the Mistral website.
api_key = os.getenv("MISTRAL_API_KEY")

# Mistral API endpoint for listing models
models_url = "https://api.mistral.ai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
}

response = requests.get(models_url, headers=headers)

if response.status_code == 200:
    models = response.json()
    #print_json_keys(models)
    for key, value in models.items():
        if key == "data":
            for item in value:
                print(item["id"])
else:
    print(f"Failed to fetch models: {response.status_code} {response.text}")

import json


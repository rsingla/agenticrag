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


'''
This is the list as of 2024-07-29

open-mistral-7b
mistral-tiny
mistral-tiny-2312
open-mistral-nemo
open-mistral-nemo-2407
mistral-tiny-2407
mistral-tiny-latest
open-mixtral-8x7b
mistral-small
mistral-small-2312
open-mixtral-8x22b
open-mixtral-8x22b-2404
mistral-small-2402
mistral-small-latest
mistral-small-2409
mistral-medium-2312
mistral-medium
mistral-medium-latest
mistral-large-2402
mistral-large-2407
mistral-large-latest
codestral-2405
codestral-latest
codestral-mamba-2407
open-codestral-mamba
codestral-mamba-latest
pixtral-12b-2409
pixtral-12b
pixtral-12b-latest
mistral-embed
'''


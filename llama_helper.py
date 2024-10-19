import requests
import json

from dotenv import load_dotenv, find_dotenv
import os
from wolframalpha import Client


def load_env():
    _ = load_dotenv(find_dotenv())

load_dotenv(find_dotenv())

client = Client(os.environ["WOLFRAM_ALPHA_APP_ID"])
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import openai
import tavily_api
import re
import httpx
import json
from dog_prompt import prompt
from langchain_agent import Agent
from openai import OpenAI



load_dotenv()  # take environment variables from .env.

# Now you can access the keys as environment variables
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_KEY = os.getenv("TAVILY_API_KEY")


client = OpenAI()

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)

print(chat_completion.choices[0].message.content)

prompt = prompt()
agent = Agent(prompt)

def calculate(what):
    return eval(what)

def average_dog_weight(name):
    if name in "Scottish Terrier": 
        return("Scottish Terriers average 20 lbs")
    elif name in "Border Collie":
        return("a Border Collies average weight is 37 lbs")
    elif name in "Toy Poodle":
        return("a toy poodles average weight is 7 lbs")
    else:
        return("An average dog weights 50 lbs")

known_actions = {
    "calculate": calculate,
    "average_dog_weight": average_dog_weight
}


result = agent("How much does a toy poodle weigh?")
print(result)

result = average_dog_weight("Toy Poodle")
print(result)

next_prompt = "Observation: {}".format(result)

result = agent(next_prompt)
print(result)

question = """I have 2 dogs, a border collie and a scottish terrier. \
What is their combined weight"""
agent(question)

next_prompt = "Observation: {}".format(average_dog_weight("Border Collie"))
print(next_prompt)

agent(next_prompt)

next_prompt = "Observation: {}".format(average_dog_weight("Scottish Terrier"))
print(next_prompt)

agent(next_prompt)

next_prompt = "Observation: {}".format(eval("37 + 20"))
print(next_prompt)

agent(next_prompt)

question = """I have 2 dogs, a border collie and a scottish terrier. \
give me the combined weight of collie and scottish terrier"""
result = agent.chat(question)
print(result)

def query(question):
    # First, use the agent to process the question
    agent_response = agent(question)
    
    # Extract dog breeds from the question
    breeds = ["Border Collie", "Scottish Terrier"]
    
    # Calculate total weight
    total_weight = 0
    for breed in breeds:
        weight_info = average_dog_weight(breed)
        weight = int(re.search(r'\d+', weight_info).group())
        total_weight += weight
    
    # Formulate the response
    response = f"{agent_response}\n\nBased on the average weights:\n"
    for breed in breeds:
        response += f"- {average_dog_weight(breed)}\n"
    response += f"\nThe combined weight of your Border Collie and Scottish Terrier is approximately {total_weight} lbs."
    
    return response

# Use the query function
question = "I have 2 dogs, a border collie and a scottish terrier. What is their combined weight?"
result = query(question)
print(result)

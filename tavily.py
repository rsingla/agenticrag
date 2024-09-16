from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
import json

import os
_ = load_dotenv()


def search_tavily(query):
    tool = TavilySearchResults(max_results=4) #increased number of results
    print(type(tool))
    print(tool.name)
    response = tool.run(query)

    return response

def search_tavily_2(query):
    tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        include_images=True,
        )
   
    questions = {"query": query}

    # Perform a search
    results = tool.invoke(questions)

    return results

if __name__ == "__main__":
    query = "How is the weather in Chandler, AZ?"
    response = search_tavily(query)

    print("Response 1:")
    print(json.dumps(response, indent=4))

    query = "What is the capital of France?"
    response2 = search_tavily_2(query)

    print("Response 2:")
   
    print(json.dumps(response2, indent=4))

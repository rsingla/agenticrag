# libraries
from dotenv import load_dotenv
import os
from tavily import TavilyClient
from browser_search import query_search, scrape_weather_info
from pretty_print import pretty_print
import re

# load environment variables from .env file
_ = load_dotenv()

# connect
client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

city = "Chandigarh"

query = f"""
    what is the current weather in {city}?
    Should I travel there today?
    "weather.com"
"""

url = query_search(query)
data= scrape_weather_info(url)

print(str(data.body)[:50000]) # limit long outputs

weather_data = []
for tag in data.find_all(['h1', 'h2', 'h3', 'p']):
    text = tag.get_text(" ", strip=True)
    weather_data.append(text)

# combine all elements into a single string
weather_data = "\n".join(weather_data)

# remove all spaces from the combined text
weather_data = re.sub(r'\s+', ' ', weather_data)
    
print(f"Website: {url}\n\n")
print(weather_data)

# run search
result = client.search(query, max_results=1)

# print first result
data = result["results"][0]["content"]

print(pretty_print(data))
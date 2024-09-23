from mistralai.client import MistralClient
from mistralai.models.chatcompletionrequest import ChatMessage

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-tiny"

client = MistralClient(api_key=api_key)

messages = [
    ChatMessage(role="user",
    content="Who is the most renowned French painter?")
]
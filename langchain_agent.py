from openai import OpenAI

class Agent:
    def __init__(self, prompt):
        self.prompt = prompt
        self.client = OpenAI()  # Initialize the OpenAI client

    def __call__(self, message):
        return self.chat(message)

    def chat(self, message):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message.content
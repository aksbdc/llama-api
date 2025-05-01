import os
from llama_api_client import LlamaAPIClient

client = LlamaAPIClient(
    api_key=os.environ.get("LLAMA_API_KEY"),
    base_url="https://api.llama.com/",
)

response = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[
        {"role": "user", "content": "What is the AI Resource Program @ Alaska SBDC?"},
    ],
)

print(response)
import os
from llama_api_client import LlamaAPIClient

client = LlamaAPIClient(
    api_key=os.environ.get("LLAMA_API_KEY"),  # This is the default and can be omitted
)

create_chat_completion_response = client.chat.completions.create(
    messages=[
        {
            "content": "string",
            "role": "user",
        }
    ],
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
)
print(create_chat_completion_response.completion_message)
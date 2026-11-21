import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.responses import response_usage

load_dotenv()

base_url = os.getenv("LLM_BASE_URL")
api_key = os.getenv("LLM_API_KEY")
model = os.getenv("LLM_MODEL")

client = OpenAI(base_url=base_url, api_key=api_key)

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Give me 3 YouTube niche ideas"}
    ],
)

print(response.choices[0].message.content)
print(response.usage.total_tokens)
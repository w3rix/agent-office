import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url = os.getenv("LLM_BASE_URL"),
    api_key = os.getenv("LLM_API_KEY"),
)
model = os.getenv("LLM_MODEL")

SYSTEM_PROMPT = """You are a YouTube niche researcher.
Return ONLY valid JSON, no markdown, no explanation.
Use exactly this shape:
{
    "niches": [
        {"name": "string", "target_audience": "string", "why_it_works": "one sentence", "competition": "low | medium | high"}
    ]
}"""

response = client.chat.completions.create(
    model = model,
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Give me 3 faceless YouTube niche ideas."},
    ],
    temperature = 0.7,
    max_tokens = 500,
)

raw = response.choices[0].message.content

try:
    data = json.loads(raw)
except json.JSONDecodeError:
    print("Model did not return valid JSON:")
    print(raw)
    raise

for niche in data["niches"]:
    print(f"- {niche['name']} -> {niche['target_audience']} -> {niche['competition']}")

print(f"Tokens used: {response.usage.total_tokens}")


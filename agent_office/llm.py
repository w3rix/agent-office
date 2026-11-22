import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)
_model = os.getenv("LLM_MODEL")

def ask(prompt: str, system: str | None = None,
        temperature: float = 0.7, max_tokens: int = 1000) -> str:
    """Send a prompt to the LLM and return the text answer."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    response = _client.chat.completions.create(
        model=_model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

def clean_json_text(text: str) -> str:
    """Remove the  ```json fences that models sometimes add. """
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n",1)[1]
        text = text.split("```",1)[0]
    return text.strip()

def ask_json(prompt: str, system: str,
             temperature: float = 0.3, max_tokens: int = 1000) -> dict:
    """Ask the LLM and parse its answer as JSON."""
    raw = ask(prompt, system, temperature, max_tokens)
    return json.loads(clean_json_text(raw))


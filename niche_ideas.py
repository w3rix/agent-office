from llm import ask_json

SYSTEM_PROMPT = """You are a YouTube niche researcher.
Return ONLY valid JSON, no markdown, no explanation.
Use exactly this shape:
{
    "niches": [
        {"name": "string", "target_audience": "string", 
        "why_it_works": "one sentence", "competition": "low | medium | high"}
    ]
}"""

data = ask_json("Give me 3 faceless YouTube niche ideas.",
                SYSTEM_PROMPT,
                temperature=0.7,
                max_tokens=500,
)

for niche in data["niches"]:
    print(f"-{niche['name']} -> {niche['target_audience']} ({niche['competition']})")
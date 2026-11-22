# agent-office

A multi-agent system that researches, scripts, edits and reviews YouTube content.
Built step by step as a learning project.

## Status
- [x] Phase 0: LLM basics (API calls, system prompts, JSON output)
- [ ] Phase 1: Niche research agent (YouTube Data API) ← in progress
- [ ] Phase 2: Script writer + reviewer agents
- [ ] Phase 3: Media pipeline (TTS, FFmpeg, subtitles)
- [ ] Phase 4: Orchestration + approval bot
- [ ] Phase 5: Publishing + analytics feedback
- [ ] Phase 6: Deployment (home server, then AWS)

## Project structure
```
agent-office/
├── agent_office/        # project code (package)
│   ├── llm.py           # shared LLM client: ask(), ask_json()
│   └── youtube.py       # YouTube Data API: search, video stats, subscriber counts
├── scripts/             # runnable experiments
│   ├── hello_llm.py
│   ├── niche_ideas.py
│   └── explore_niche.py
└── requirements.txt
```

## Setup
1. Python 3.12+
2. `python -m venv .venv` and activate it
3. `python -m pip install -r requirements.txt`
4. Create a `.env` file in the project root:
   ```
   LLM_BASE_URL=https://openrouter.ai/api/v1
   LLM_API_KEY=your-openrouter-key
   LLM_MODEL=nvidia/nemotron-3-ultra-550b-a55b:free
   YOUTUBE_API_KEY=your-google-cloud-key
   ```
   The YouTube key comes from Google Cloud Console with **YouTube Data API v3** enabled.
   Restrict the key to that API.

## Running scripts
Run from the project root with `-m` (dots instead of slashes, no `.py`):
```
python -m scripts.explore_niche
```

| Script | What it does |
| --- | --- |
| `hello_llm.py` | First raw LLM call |
| `niche_ideas.py` | Structured JSON niche ideas from the LLM |
| `explore_niche.py` | Top recent long-form videos for a query, with views-to-subscribers ratio and outlier count |

## Notes
- YouTube search uses 1 of ~100 daily search calls per run; video and channel lookups cost 1 unit each.
- Free OpenRouter models are rate limited (20 requests/minute, 50/day on an unfunded account).
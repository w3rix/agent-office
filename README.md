# agent-office

A multi-agent system that researches, scripts, edits and reviews YouTube content.
Built step by step as a learning project.

## Status
- [x] Phase 0: LLM basics (API calls, system prompts, JSON output)
- [ ] Phase 1: Niche research agent (YouTube Data API)
- [ ] Phase 2: Script writer + reviewer agents
- [ ] Phase 3: Media pipeline (TTS, FFmpeg, subtitles)
- [ ] Phase 4: Orchestration + approval bot
- [ ] Phase 5: Publishing + analytics feedback
- [ ] Phase 6: AWS deployment

## Setup
1. Python 3.12+
2. `python -m venv .venv` and activate it
3. `pip install -r requirements.txt`
4. Create a `.env` file in the project root:
   ```
   LLM_BASE_URL=https://openrouter.ai/api/v1
   LLM_API_KEY=your-key
   LLM_MODEL=nvidia/nemotron-3-ultra-550b-a55b:free
   ```

## Scripts
- `hello_llm.py`: first raw LLM call
- `niche_ideas.py`: structured JSON niche ideas
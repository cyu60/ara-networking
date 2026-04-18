# Ara Networking Agent

Single-agent example from the [Ara Hackathon Tour 2026](https://github.com/cyu60/ara-ai-computer) — a chat-based personal CRM and follow-up drafter running on the [Ara](https://ara.so) agentic operating system.

Part of the **Aragrams** — reference projects built by [DayDreamers](https://daydreamers.club) to show what's possible with agent-first development.

## What it does

Remember everyone you meet, log LinkedIn profiles, and draft warm follow-up emails. Text the agent after a meeting ("Met Priya at YC Demo Day — Anthropic, works on MCP, wants to chat about agent evals") and it:

- Captures the person, company, role, and context into a persistent contact log
- Pulls and summarizes LinkedIn profiles when you paste a URL
- Answers queries like "who did I meet this month who works on agents?"
- Drafts warm, specific follow-up emails that reference what you actually talked about
- Keeps the whole roster as JSON on the sandbox filesystem — no CRM to open

No spreadsheets, no tagging UI — just text the agent like a friend with a perfect memory for people.

## Architecture

```
Browser (index.html)
   ↓
/api/run (Vercel serverless function)
   ↓
Ara API (api.ara.so) — Bearer ARA_RUNTIME_KEY
   ↓
networking-agent subagent running in a sandboxed Python runtime
```

## Local dev

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install ara-sdk
export ARA_ACCESS_TOKEN=<your_token>

python3 app.py setup                             # registers the app → returns APP_ID
python3 app.py deploy --on-existing update       # pushes the agent definition
python3 app.py run --workflow networking-agent --message "Met Priya at YC Demo Day — Anthropic, works on MCP"
```

## Deploy

This repo is wired to Vercel. On push to `main`:

1. Vercel builds the static frontend + `api/run.js` edge function.
2. The function proxies `/api/run` calls to `https://api.ara.so/v1/apps/<APP_ID>/run` using `ARA_RUNTIME_KEY`.
3. The Ara runtime spins up the `networking-agent` sandbox on demand.

## License

MIT

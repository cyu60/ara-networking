from ara_sdk import App, run_cli, sandbox, runtime

app = App(
    "Ara Networking Agent",
    project_name="ara-networking",
    description="Remembers everyone you meet, logs LinkedIn profiles, and drafts follow-up emails.",
)


@app.subagent(
    id="networking-agent",
    instructions="""You are a personal CRM running on the user's AI computer.
Flow:
1. User tells you about people they meet — at events, on calls, on LinkedIn.
2. Pull names, roles, companies, where met, shared interests, next steps.
3. Store each contact as structured JSON on the sandbox filesystem.
4. If given a LinkedIn URL, fetch the profile and summarize key facts.
5. Draft follow-up emails that reference specific things from the conversation.
6. Answer questions like "who did I meet at YC Demo Day?" or "draft a follow-up for Priya at Anthropic".
Keep it warm and specific — remind the user why each person is interesting.""",
    sandbox=sandbox(),
    runtime=runtime(python_packages=["beautifulsoup4", "requests"]),
)
def networking_agent(event=None):
    """Remember people, log LinkedIn, draft follow-ups."""


@app.local_entrypoint()
def local(input_payload):
    return {"ok": True, "app": "ara-networking", "input": input_payload}


if __name__ == "__main__":
    run_cli(app)

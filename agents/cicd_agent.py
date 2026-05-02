from agents.common_llm import query_llm


def debug_pipeline(logs: str) -> str:
    prompt = f"""
You are a CI/CD expert.

Respond ONLY in this format:

Failure Step: <step>
Root Cause: <one line>
Fix: <clear fix>

Logs:
{logs}
"""
    return query_llm(prompt)

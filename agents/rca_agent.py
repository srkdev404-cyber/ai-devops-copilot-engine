from agents.common_llm import query_llm


def run_rca(logs: str) -> str:
    prompt = f"""
You are a senior SRE.

Analyze production logs.

Respond ONLY in this format:

Root Cause: <one line>
Impact: <system/user impact>
Fix: <clear actionable fix>

Logs:
{logs}
"""
    return query_llm(prompt)

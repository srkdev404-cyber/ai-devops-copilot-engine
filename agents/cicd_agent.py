from agents.common_llm import query_llm

def debug_pipeline(logs, context=""):
    prompt = f"""
You are a CI/CD expert.

Analyze pipeline failure logs:
- Identify failure step
- Root cause
- Fix suggestion

Context:
{context}

Logs:
{logs}
"""
    return query_llm(prompt)

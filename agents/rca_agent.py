from agents.common_llm import query_llm

def run_rca(logs, context=""):
    prompt = f"""
You are a DevOps expert.

Analyze the logs and find:
1. Root cause
2. Impact
3. Fix

Context:
{context}

Logs:
{logs}
"""
    return query_llm(prompt)

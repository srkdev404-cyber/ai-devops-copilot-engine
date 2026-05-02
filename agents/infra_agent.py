from agents.common_llm import query_llm

def generate_terraform(infra_json):
    prompt = f"""
Convert AWS infrastructure into Terraform.

Also:
- Improve readability
- Add best practices

Input:
{infra_json}
"""
    return query_llm(prompt)

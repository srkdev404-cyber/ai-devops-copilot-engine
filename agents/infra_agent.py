from agents.common_llm import query_llm


def generate_terraform(infra_data: str) -> str:
    prompt = f"""
You are a DevOps engineer.

Convert the following AWS infrastructure into Terraform.

Also suggest improvements.

Input:
{infra_data}
"""
    return query_llm(prompt)

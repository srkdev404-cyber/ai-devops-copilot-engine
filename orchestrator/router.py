from agents.rca_agent import run_rca
from agents.cicd_agent import debug_pipeline
from agents.infra_agent import generate_terraform


def route(query: str, data: str) -> str:
    q = query.lower()

    if "pipeline" in q or "build" in q:
        return debug_pipeline(data)

    elif "terraform" in q or "infra" in q:
        return generate_terraform(data)

    else:
        return run_rca(data)

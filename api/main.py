from fastapi import FastAPI
from orchestrator.router import route

app = FastAPI()

@app.post("/copilot")
def copilot(query: str, data: str):
    result = route(query, data)
    return {"response": result}

from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.router import route
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)


class CopilotRequest(BaseModel):
    query: str
    data: str


@app.post("/copilot")
def copilot(req: CopilotRequest):
    logging.info(f"Query: {req.query}")

    result = route(req.query, req.data)

    logging.info(f"Response: {result}")

    return {"response": result}

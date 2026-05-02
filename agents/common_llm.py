import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_llm(prompt: str, model="mistral"):
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

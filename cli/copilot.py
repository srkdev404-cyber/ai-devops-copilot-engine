import requests
import sys

query = sys.argv[1]

# Load sample data (can replace later with real logs)
with open("data/logs.json") as f:
    data = f.read()

try:
    res = requests.post(
        "http://localhost:8000/copilot",
        json={
            "query": query,
            "data": data
        }
    )

    print(res.json()["response"])

except Exception:
    print("❌ API not running. Start FastAPI server first.")

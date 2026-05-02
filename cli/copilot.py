import requests
import sys

query = sys.argv[1]

with open("data/logs.json") as f:
    data = f.read()

res = requests.post("http://localhost:8000/copilot", params={
    "query": query,
    "data": data
})

print(res.json()["response"])

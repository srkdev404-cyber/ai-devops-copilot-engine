import requests
from typing import Optional
from config.settings import OLLAMA_URL, DEFAULT_MODEL, TIMEOUT


def clean_output(response: str) -> str:
    """
    Extract only structured DevOps output:
    Root Cause / Impact / Fix
    """
    if not response:
        return ""

    lines = response.split("\n")
    result = []

    for line in lines:
        line = line.strip()
        if any(key in line for key in ["Root Cause", "Impact", "Fix"]):
            result.append(line)

    return "\n".join(result)


def query_llm(prompt: str, model: Optional[str] = None) -> str:
    """
    Send prompt to Ollama and return cleaned structured response
    """

    selected_model = model if model else DEFAULT_MODEL

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": selected_model,
                "prompt": prompt,
                "stream": False
            },
            timeout=TIMEOUT
        )

        response.raise_for_status()

        raw_output = response.json().get("response", "").strip()

        cleaned = clean_output(raw_output)

        if not cleaned:
            return (
                "⚠️ Unable to extract structured RCA.\n"
                f"Raw Output:\n{raw_output[:500]}"
            )

        return cleaned

    except requests.exceptions.Timeout:
        return "⚠️ LLM request timed out."

    except requests.exceptions.ConnectionError:
        return "❌ Cannot connect to Ollama. Is it running?"

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

import requests
import os
from dotenv import load_dotenv

#Load API key from .env file
env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=env_path)

# Get API key from environment (safer)
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise RuntimeError("❌ OPENROUTER_API_KEY is not set. Check your .env file or environment variables.")

print("🔑 Loaded API Key:", API_KEY[:6] + "..." if API_KEY else "None")

# Use OpenRouter endpoint
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def query_openrouter(prompt: str, model: str = "mistralai/mistral-small-3.2-24b-instruct") -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a quiz generator that outputs clean multiple-choice questions."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"OpenRouter error {response.status_code}: {response.text}")

    data = response.json()
    return data["choices"][0]["message"]["content"]

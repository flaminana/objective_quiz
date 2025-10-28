import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt: str, model: str = "mistral") -> str:
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream":False #disable streaming to get clean JSON
    })
    print("🔊 Raw Ollama response:", response.text) #log full response
    
    return response.json()["response"]
# src/llm_client.py
import os
import httpx
from dotenv import load_dotenv

# Load env variables
load_dotenv()
API_KEY = os.getenv("AIML_API_KEY")

BASE_URL = "https://api.aimlapi.com/v1/chat/completions"


async def generate_response(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    Send a prompt to the LLM API and return the generated response.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

    return data["choices"][0]["message"]["content"].strip()

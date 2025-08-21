# test_api.py
import time
from src.utils.config import AIML_API_KEY
from openai import OpenAI
from openai import OpenAIError

MAX_RETRIES = 3
RETRY_DELAY = 60  # seconds to wait before retrying after rate limit

def test_aiml_api():
    client = OpenAI(
        base_url="https://api.aimlapi.com/v1",
        api_key=AIML_API_KEY
    )
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": "Write a one-sentence story about numbers."}]
            )
            print("✅ API call successful!")
            print("Response:", response.choices[0].message.content)
            break  # exit loop on success
        except OpenAIError as e:
            if "rate limit" in str(e).lower() and attempt < MAX_RETRIES:
                print(f"⚠️ Rate limit hit. Retrying in {RETRY_DELAY} seconds... (Attempt {attempt}/{MAX_RETRIES})")
                time.sleep(RETRY_DELAY)
            else:
                print("❌ API call failed:", str(e))
                break

if __name__ == "__main__":
    test_aiml_api()

from src.utils.config import AIML_API_KEY

if AIML_API_KEY:
    print("✅ AIML API Key loaded successfully!")
else:
    print("❌ Failed to load AIML API Key. Check your .env file.")

# src/utils/config.py

import os
from dotenv import load_dotenv

load_dotenv()

AIML_API_KEY = os.getenv("AIML_API_KEY")

WHISPER_MODEL = "small"
TTS_VOICE = "default"
TTS_RATE = 150

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
SYNTHETIC_DATA_PATH = os.path.join(DATA_DIR, "synthetic_dataset.csv")
FAQ_PATH = os.path.join(DATA_DIR, "faq_context.json")

LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

MAX_ANSWER_LENGTH = 500

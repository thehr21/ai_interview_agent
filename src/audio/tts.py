import os
from elevenlabs import generate, play, set_api_key

# Set your ElevenLabs API key here or via environment variable
API_KEY = os.getenv("ELEVENLABS_API_KEY")
set_api_key(API_KEY)

class TextToSpeech:
    def __init__(self, voice="alloy"):
        """
        Initialize TTS with a specific ElevenLabs voice.
        Default 'alloy' is a neutral, clear voice.
        """
        self.voice = voice

    def speak(self, text):
        """
        Generate speech from text and play it immediately.
        """
        if not text.strip():
            return  # skip empty text

        audio = generate(text=text, voice=self.voice, model="eleven_monolingual_v1")
        play(audio)

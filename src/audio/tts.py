# src/audio/tts.py
import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, play

# Load environment variables
load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
if not API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found in environment variables. Please add it to your .env file.")

# Initialize ElevenLabs client
client = ElevenLabs(api_key=API_KEY)

class TextToSpeech:
    def __init__(self, voice_name="Rachel"):
        self.voice_name = voice_name

        # Fetch all voices
        response = client.voices.get_all()
        all_voices = response.voices

        # Debug: print all available voices
        print("Available voices:")
        for v in all_voices:
            print(f"- {v.name} (ID: {v.voice_id})")

        # Try to select the requested voice
        self.voice = next((v for v in all_voices if v.name.lower() == voice_name.lower()), None)

        if not self.voice:
            print(f"Voice '{voice_name}' not found. Using default voice: Rachel")
            self.voice = next((v for v in all_voices if v.name.lower() == "rachel"), all_voices[0])

    def speak(self, text: str):
        if not text.strip():
            return

        try:
            audio = client.text_to_speech.convert(
                text=text,
                voice_id=self.voice.voice_id,
                model_id="eleven_multilingual_v2",
                output_format="mp3_44100_128"
            )
            play(audio)
        except Exception as e:
            print(f"TTS Error: {e}")

# src/audio/stt.py
import whisper
import sounddevice as sd
import numpy as np
from scipy.io import wavfile

class SpeechToText:
    def __init__(self, model_name="base"):
        """
        Initialize Whisper model.
        model_name options: tiny, base, small, medium, large
        """
        print(f"Loading Whisper model '{model_name}'...")
        self.model = whisper.load_model(model_name)
        print("Model loaded successfully.")

    def record_audio(self, duration=5, fs=16000, filename="temp_audio.wav"):
        """
        Record audio from microphone and save as WAV file.
        duration: seconds
        fs: sampling frequency
        """
        print(f"Recording for {duration} seconds...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        # Normalize audio to int16 for wavfile.write
        audio_int16 = np.int16(audio / np.max(np.abs(audio)) * 32767)
        wavfile.write(filename, fs, audio_int16)
        print(f"Audio saved as {filename}")
        return filename

    def transcribe_file(self, filename):
        """
        Transcribe an audio file using Whisper
        """
        print(f"Transcribing {filename} ...")
        result = self.model.transcribe(filename)
        text = result['text']
        print(f"Transcription: {text}")
        return text

    def record_and_transcribe(self, duration=5, fs=16000):
        """
        Record audio from microphone and transcribe immediately
        """
        filename = self.record_audio(duration, fs)
        return self.transcribe_file(filename)


# Example usage
if __name__ == "__main__":
    stt = SpeechToText(model_name="base")
    text = stt.record_and_transcribe(duration=5)
    print(f"Recognized Text: {text}")

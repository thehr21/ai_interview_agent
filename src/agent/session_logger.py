import os
import json
import csv
from datetime import datetime

LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)
JSON_LOG_PATH = os.path.join(LOGS_DIR, "interviews.json")
CSV_LOG_PATH = os.path.join(LOGS_DIR, "interviews.csv")
TRANSCRIPT_PATH = os.path.join(LOGS_DIR, "transcript.txt")


class SessionLogger:
    def log_json(self, session_data, filename=None):
        """Append session to JSON file"""
        path = filename or JSON_LOG_PATH
        all_data = []

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    all_data = json.load(f)
                except json.JSONDecodeError:
                    all_data = []

        all_data.append(session_data)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4)
        print(f"Session saved to JSON: {path}")

    def log_csv(self, session_data, filename=None):
        """Append session to CSV file"""
        path = filename or CSV_LOG_PATH
        file_exists = os.path.isfile(path)

        with open(path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["timestamp", "question", "answer"])

            for key, value in session_data.items():
                if key == "metadata":
                    continue
                writer.writerow([value["timestamp"], value["question"], value["answer"]])
        print(f"Session saved to CSV: {path}")

    def log_transcript(self, session_data, filename=None):
        """Save a human-readable transcript"""
        path = filename or TRANSCRIPT_PATH
        with open(path, "w", encoding="utf-8") as f:
            for key, value in session_data.items():
                if key == "metadata":
                    continue
                f.write(f"{value['timestamp']} - Q: {value['question']}\n")
                f.write(f"{value['timestamp']} - A: {value['answer']}\n\n")
        print(f"Transcript saved to: {path}")

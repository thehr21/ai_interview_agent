import random
from datetime import datetime
from src.audio import stt, tts  # We'll create these modules for speech

class InterviewAgent:
    def __init__(self, min_answer_length=5, use_speech=True):
        self.questions = [
            "What is your full name and background?",
            "Why are you interested in joining the program?",
            "What’s your experience with data science or AI?",
            "What are your short-term and long-term goals?",
            "Are you ready to start immediately? If not, when?"
        ]
        self.responses = {}
        self.rephrase_prompts = [
            "Sorry, I didn't catch that. Could you please elaborate?",
            "Could you provide a bit more detail?",
            "I’m not sure I understood. Could you rephrase your answer?",
        ]
        self.min_answer_length = min_answer_length
        self.use_speech = use_speech

    def ask_question(self, question):
        attempt = 0

        # Speak the question if TTS enabled
        if self.use_speech:
            tts.speak(question)
            answer = stt.listen()
        else:
            answer = input(f"{question}\n> ").strip()

        # Fallback to text input if STT fails
        if not answer:
            answer = input(f"{question}\n> ").strip()

        while len(answer) < self.min_answer_length:
            prompt = random.choice(self.rephrase_prompts)
            if self.use_speech:
                tts.speak(prompt)
            else:
                print(prompt)
            if self.use_speech:
                answer = stt.listen()
            else:
                answer = input(f"{question}\n> ").strip()

            # Fallback again
            if not answer:
                answer = input(f"{question}\n> ").strip()

            attempt += 1

        return answer

    def start_interview(self):
        print("Welcome to the LunarTech AI Interview!\n")
        if self.use_speech:
            tts.speak("Welcome to the LunarTech AI Interview!")

        start_time = datetime.now()

        for i, question in enumerate(self.questions, 1):
            answer = self.ask_question(question)
            timestamp = datetime.now().isoformat()
            self.responses[f"Q{i}"] = {
                "question": question,
                "answer": answer,
                "timestamp": timestamp
            }

        end_time = datetime.now()
        self.responses["metadata"] = {
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "total_questions": len(self.questions)
        }

        print("\nInterview complete!:\n")
        if self.use_speech:
            tts.speak("The interview has concluded. All your responses have been recorded successfully.")

        for qid, data in self.responses.items():
            if qid != "metadata":
                print(f"{data['question']}\nAnswer: {data['answer']}\n")
                if self.use_speech:
                    tts.speak(f"{data['question']}: {data['answer']}")

        return self.responses


if __name__ == "__main__":
    agent = InterviewAgent()
    responses = agent.start_interview()

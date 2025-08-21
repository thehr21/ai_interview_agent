import random
from datetime import datetime
from src.audio import stt, tts
from src.llm_client import call_llm  

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
        if self.use_speech:
            tts.speak(question)
            user_input = stt.listen()
        else:
            user_input = input(f"{question}\n> ").strip()

        # Fallback to text input if STT fails
        if not user_input:
            user_input = input(f"{question}\n> ").strip()

        # Enforce minimum length (re-prompt if too short)
        while len(user_input) < self.min_answer_length:
            prompt = random.choice(self.rephrase_prompts)
            if self.use_speech:
                tts.speak(prompt)
                user_input = stt.listen()
            else:
                print(prompt)
                user_input = input(f"{question}\n> ").strip()

            if not user_input:
                user_input = input(f"{question}\n> ").strip()

        llm_reply = call_llm(user_input)

        if self.use_speech:
            tts.speak(llm_reply)
        else:
            print(f"\n🤖 LLM: {llm_reply}\n")

        return user_input, llm_reply

    def start_interview(self):
        print("Welcome to the LunarTech AI Interview!\n")
        if self.use_speech:
            tts.speak("Welcome to the LunarTech AI Interview!")

        start_time = datetime.now()

        for i, question in enumerate(self.questions, 1):
            answer, llm_reply = self.ask_question(question)
            timestamp = datetime.now().isoformat()

            self.responses[f"Q{i}"] = {
                "question": question,
                "answer": answer,
                "llm_reply": llm_reply,
                "timestamp": timestamp
            }

        end_time = datetime.now()
        self.responses["metadata"] = {
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "total_questions": len(self.questions)
        }

        print("\nInterview complete!\n")
        if self.use_speech:
            tts.speak("The interview has concluded. All your responses have been recorded successfully.")

        # Print transcript
        for qid, data in self.responses.items():
            if qid != "metadata":
                print(f"{data['question']}\nUser: {data['answer']}\n🤖 LLM: {data['llm_reply']}\n")

        return self.responses


if __name__ == "__main__":
    agent = InterviewAgent()
    responses = agent.start_interview()

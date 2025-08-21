from src.agent.conversational_flow import InterviewAgent

def run_interview():
    agent = InterviewAgent()
    responses = agent.start_interview()

    import json
    import os

    output_path = os.path.join("logs", "latest_interview.json")
    os.makedirs("logs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(responses, f, indent=4)
    
    print(f"\nResponses saved to {output_path}")

if __name__ == "__main__":
    run_interview()

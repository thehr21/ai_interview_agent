from src.agent.conversational_flow import InterviewAgent
from src.agent.session_logger import SessionLogger

def run_interview():
    # Start the interview
    agent = InterviewAgent()
    responses = agent.start_interview()

    # Initialize the session logger
    logger = SessionLogger()

    # Log responses in JSON, CSV, and human-readable transcript
    logger.log_json(responses)
    logger.log_csv(responses)
    logger.log_transcript(responses)

    print("\nAll responses saved successfully in JSON, CSV, and transcript files.")

if __name__ == "__main__":
    run_interview()

from services.gemini_service import generate_response
from utils.prompts import INTERVIEW_PROMPT


class InterviewAgent:

    def generate_questions(self, role):

        prompt = f"""
{INTERVIEW_PROMPT}

Job Role:

{role}
"""

        try:
            return generate_response(prompt)

        except Exception as e:
            return f"⚠️ Interview Agent Error:\n\n{e}"
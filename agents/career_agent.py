from services.gemini_service import generate_response
from utils.prompts import CAREER_PROMPT


class CareerAgent:

    def suggest(self, career_goal):

        prompt = f"""
{CAREER_PROMPT}

Career Goal:

{career_goal}
"""

        try:
            return generate_response(prompt)

        except Exception as e:
            return f"⚠️ Career Agent Error:\n\n{e}"
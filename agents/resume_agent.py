from services.gemini_service import generate_response
from utils.prompts import RESUME_PROMPT


class ResumeAgent:

    def analyze(self, resume_text):

        prompt = f"""
{RESUME_PROMPT}

Resume:

{resume_text}
"""

        try:
            return generate_response(prompt)

        except Exception as e:
            return f"⚠️ Resume Agent Error:\n\n{e}"
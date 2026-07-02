from agents.resume_agent import ResumeAgent
from agents.career_agent import CareerAgent
from agents.interview_agent import InterviewAgent


class ManagerAgent:

    def __init__(self):
        self.resume = ResumeAgent()
        self.career = CareerAgent()
        self.interview = InterviewAgent()

    def route(self, user_input, resume_text=None):

        text = user_input.lower()

        if "resume" in text or "cv" in text:

            if resume_text:
                return self.resume.analyze(resume_text)

            return "⚠️ Please upload your resume first."

        elif "interview" in text:
            return self.interview.generate_questions(user_input)

        else:
            return self.career.suggest(user_input)
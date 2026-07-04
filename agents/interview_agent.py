from careerpilot_mcp.client import call_tool


class InterviewAgent:

    def generate_questions(self, role):

        try:
            return call_tool(
                "interview_questions",
                {
                    "role": role
                }
            )

        except Exception as e:
            return f"⚠️ Interview Agent Error:\n\n{e}"
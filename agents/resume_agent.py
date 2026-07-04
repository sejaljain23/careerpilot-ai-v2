from careerpilot_mcp.client import call_tool


class ResumeAgent:

    def analyze(self, resume_text):

        try:
            return call_tool(
                "resume_analysis",
                {
                    "resume_text": resume_text
                }
            )

        except Exception as e:
            return f"⚠️ Resume Agent Error:\n\n{e}"
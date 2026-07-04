from careerpilot_mcp.client import call_tool


class CareerAgent:

    def suggest(self, career_goal):

        return call_tool(
            "career_guidance",
            {
                "career_goal": career_goal
            }
        )
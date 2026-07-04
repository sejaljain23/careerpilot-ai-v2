
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from fastmcp import FastMCP

from services.gemini_service import generate_response
from utils.prompts import (
    RESUME_PROMPT,
    CAREER_PROMPT,
    INTERVIEW_PROMPT,
)

mcp = FastMCP("CareerPilot MCP")


@mcp.tool()
def resume_analysis(resume_text: str) -> str:
    """
    Analyze a resume and return ATS feedback.
    """
    prompt = f"""
{RESUME_PROMPT}

Resume:

{resume_text}
"""
    return generate_response(prompt)


@mcp.tool()
def career_guidance(career_goal: str) -> str:
    """
    Provide career guidance.
    """
    prompt = f"""
{CAREER_PROMPT}

Career Goal:

{career_goal}
"""
    return generate_response(prompt)


@mcp.tool()
def interview_questions(role: str) -> str:
    """
    Generate interview questions.
    """
    prompt = f"""
{INTERVIEW_PROMPT}

Role:

{role}
"""
    return generate_response(prompt)


if __name__ == "__main__":
    mcp.run()
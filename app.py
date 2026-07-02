import re
import streamlit as st
from dotenv import load_dotenv

from tools.pdf_reader import extract_text_from_pdf

from agents.resume_agent import ResumeAgent
from agents.career_agent import CareerAgent
from agents.interview_agent import InterviewAgent
from agents.manager_agent import ManagerAgent

from memory.session_memory import SessionMemory
import memory.session_memory as sm



from adk.career_adk import start_adk

load_dotenv()

resume_agent = ResumeAgent()
career_agent = CareerAgent()
interview_agent = InterviewAgent()
manager_agent = ManagerAgent()

if "memory" not in st.session_state:
    st.session_state.memory = SessionMemory()

memory = st.session_state.memory

st.write(dir(memory))

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.markdown("""
### Your AI-Powered Career Guidance Platform

Analyze your resume, explore career paths, and prepare for interviews using **Google ADK** and **Gemini AI**.
""")

st.markdown("---")

st.success(start_adk())

st.sidebar.title("🚀 CareerPilot AI")

st.sidebar.markdown("---")

st.sidebar.subheader("👤 User")
st.sidebar.info("Welcome!")

st.sidebar.markdown("---")

st.sidebar.subheader("🤖 AI Status")
st.sidebar.success("Google ADK Ready")
st.sidebar.success("Gemini Connected")

st.sidebar.markdown("---")

st.sidebar.subheader("🧠 Session Memory")

goal = memory.get("career_goal")

if goal:
    st.sidebar.info(goal)
else:
    st.sidebar.warning("No Career Goal Yet")

st.sidebar.markdown("---")

st.sidebar.subheader("📝 Recent Questions")

history = memory.get_history()

if history:
    for question in history[-5:]:
        st.sidebar.write(f"• {question}")
else:
    st.sidebar.info("No questions yet")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Features")

st.sidebar.write("📄 Resume Analysis")
st.sidebar.write("💼 Career Coach")
st.sidebar.write("🎤 Interview Prep")
st.sidebar.write("🧠 Session Memory")

tab1, tab2, tab3, tab4 = st.tabs([
    "📄 Resume Analysis",
    "💼 Career Coach",
    "🎤 Interview Prep",
    "ℹ️ About"
])

uploaded_file = None
resume_text = None

with tab1:

    st.markdown("""
## 📄 Resume Analysis

Upload your resume in **PDF format** and receive an AI-powered evaluation.

### You will get:

- ✅ ATS Score
- ✅ Resume Strengths
- ✅ Missing Skills
- ✅ Suggested Career Roles
- ✅ Resume Improvements
- ✅ Learning Roadmap
""")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"],
        key="resume_uploader"
    )

    if uploaded_file is not None:

        resume_text = extract_text_from_pdf(uploaded_file)

        st.success(f"✅ Resume '{uploaded_file.name}' uploaded successfully!")
        st.write("**Filename:**", uploaded_file.name)

        if st.button("Analyze Resume", key="analyze_resume"):

         st.subheader("📄 Resume Text")

        st.text_area(
            "Extracted Text",
            resume_text,
            height=300
        )

        with st.spinner("🤖 Analyzing Resume..."):

         analysis = resume_agent.analyze(resume_text)

        st.subheader("📊 AI Resume Analysis")

        with st.expander("📄 View Complete AI Analysis", expanded=True):
         st.markdown(analysis)


        match = re.search(r'(\d{1,3})\s*/\s*100', analysis)

        if match:
            ats_score = int(match.group(1))
        else:
            ats_score = 80

        col1, col2 = st.columns([1, 2])

with col1:
    st.metric(
        label="📊 ATS Score",
        value=f"{ats_score}/100"
    )

with col2:
    st.write("### ATS Progress")
    st.progress(ats_score / 100)
      

with tab2:

    st.write("""
    ### 💼 Career Coach

    Ask any career-related question like:
    - I want to become a Data Scientist
    - Best roadmap for Python Developer
    - Skills required for AI Engineer
    """)

    user_query = st.text_input(
        "Ask your career question",
        placeholder="Example: I want to become a Data Scientist",
        key="career_query"
    )

    if st.button("Ask AI", key="ask_ai"):

        if user_query:

            with st.spinner("🤖 Career Agent Thinking..."):

                try:

                    memory.save("last_query", user_query)
                    memory.add_history(user_query)

                    st.write("History:", memory.get_history())

                    if "i want to become" in user_query.lower():
                        memory.save("career_goal", user_query)

                    if uploaded_file and resume_text:
                        answer = manager_agent.route(user_query, resume_text)
                    else:
                        answer = manager_agent.route(user_query)

                    st.success("CareerPilot AI Response")
                    st.markdown(answer)

                    st.markdown("### 📝 Recent Questions")

                    for question in memory.get_history()[-5:]:
                     st.write(f"• {question}")

                    goal = memory.get("career_goal")

                    if goal:
                        st.info(f"🎯 Current Career Goal: {goal}")

                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

with tab3:

    st.write("""
    ### 🎤 Interview Preparation

    Generate interview questions for any job role.

    Examples:
    - Data Analyst
    - Data Scientist
    - Python Developer
    - AI Engineer
    """)

    role = st.text_input(
        "Enter Job Role",
        placeholder="Example: Data Analyst",
        key="interview_role"
    )

    if st.button("Generate Interview Questions", key="interview_btn"):

        if role:

            with st.spinner("🤖 Generating Interview Questions..."):

                try:

                    questions = interview_agent.generate_questions(role)

                    st.success("Interview Questions Generated")
                    st.markdown(questions)

                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

    
with tab4:

    st.title("ℹ️ About CareerPilot AI")

    st.markdown("""
    ## 🚀 Project Overview

    CareerPilot AI is an AI-powered career guidance platform that helps users:

    - 📄 Analyze resumes with AI
    - 📊 Get an ATS Score
    - 💼 Receive personalized career guidance
    - 🎤 Prepare for interviews
    - 🧠 Maintain session memory for better conversations

    ---

    ## 🛠️ Tech Stack

    - Python
    - Streamlit
    - Google Gemini
    - Google ADK
    - PDF Processing
    - Session Memory

    ---

    ## 🤖 AI Agents

    ✅ Resume Agent

    Analyzes resumes and provides ATS score, strengths, weaknesses, and improvement suggestions.

    ✅ Career Agent

    Answers career-related questions and provides personalized career guidance.

    ✅ Interview Agent

    Generates interview questions for different job roles.

    ✅ Manager Agent

    Routes user requests to the appropriate AI agent.

    ---

    ## 🎯 Objective

    To provide students and professionals with an intelligent AI assistant for resume analysis, career planning, and interview preparation in one platform.

    ---

    ## 🔮 Future Scope

    - Resume vs Job Description Matching
    - PDF Report Download
    - Voice-based Career Coach
    - Job Recommendation System
    - AI Mock Interview

    ---

    ### 🚀 CareerPilot AI
    **Kaggle Capstone Project 2026**
    """)
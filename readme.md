# 🚀 CareerPilot AI

> An AI-powered career guidance platform built with **Google Gemini**, **Google ADK**, and **FastMCP** to help students and professionals improve their resumes, plan careers, and prepare for interviews.

---

## 🌟 Overview

CareerPilot AI is a multi-agent career assistant that provides intelligent career guidance using Google's latest AI technologies.

The platform enables users to:

- 📄 Analyze resumes
- 📊 Receive ATS-style feedback
- 💼 Get personalized career guidance
- 🎤 Prepare for interviews
- 🧠 Maintain conversation context using session memory

---

## ✨ Features

### 📄 Resume Analysis
- AI-powered resume evaluation
- ATS score generation
- Strengths & weaknesses
- Missing skills detection
- Resume improvement suggestions
- Downloadable PDF report

### 💼 Career Coach
- Personalized career guidance
- Learning roadmaps
- Required skills
- Technology recommendations
- Career planning

### 🎤 Interview Preparation
- Role-specific interview questions
- Technical interview preparation
- HR interview questions
- Practice guidance

### 🧠 Session Memory
- Stores recent questions
- Tracks career goals
- Improves conversation continuity

---

# 🤖 Multi-Agent Architecture

CareerPilot AI uses multiple AI agents to solve different tasks.

### Resume Agent
Analyzes resumes and generates ATS-style feedback.

### Career Agent
Provides career guidance and learning roadmaps.

### Interview Agent
Generates interview questions for different job roles.

### Manager Agent
Routes user requests to the appropriate AI agent.

---

# 🔌 FastMCP Integration

CareerPilot AI integrates the **Model Context Protocol (MCP)** using **FastMCP**.

The Streamlit application communicates with an MCP server through an MCP client.

This architecture makes the application modular and scalable.

Workflow:

```
User
    │
    ▼
Streamlit UI
    │
    ▼
FastMCP Client
    │
    ▼
CareerPilot MCP Server
    │
    ▼
Google Gemini
    │
    ▼
AI Response
```

---

# 🧠 Google ADK Integration

CareerPilot AI demonstrates Google Agent Development Kit (ADK) concepts including:

- Agent orchestration
- Multi-agent workflow
- Tool-based architecture
- AI task routing

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash
- Google ADK
- FastMCP
- PyMuPDF
- ReportLab
- dotenv

---

# 📂 Project Structure

```
CareerPilot-AI
│
├── agents/
├── careerpilot_mcp/
├── services/
├── tools/
├── utils/
├── memory/
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/sejaljain23/careerpilot-ai-v2.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🌐 Live Demo

Render Deployment

https://careerpilot-ai-v2.onrender.com

GitHub Repository

https://github.com/sejaljain23/careerpilot-ai-v2

---

# 🚀 Future Enhancements

- Job Recommendation System
- Resume vs Job Description Matching
- AI Mock Interviews
- Voice Career Coach
- Job Market Insights
- Skill Gap Analysis

---

# 👩‍💻 Author

**Sejal Jain**

Kaggle 5-Day AI Agents Capstone Project (2026)

---

# 📄 License

MIT License
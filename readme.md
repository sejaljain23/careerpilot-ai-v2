# 🚀 CareerPilot AI

> An AI-powered career assistant built using Google Gemini and AI Agents to help students improve their resumes, explore career paths, and prepare for interviews.

---

## 📌 Overview

CareerPilot AI is an intelligent career guidance platform developed as part of the **Kaggle 5-Day AI Agents: Intensive Vibe Coding Course with Google**.

The application uses multiple AI agents to analyze resumes, recommend career paths, generate interview questions, and provide personalized career guidance.

---

## ✨ Features

* 📄 Resume PDF Upload
* 🤖 AI Resume Analysis
* 📊 ATS Score Calculation
* 📈 ATS Progress Bar
* 📥 Download Resume Analysis Report (PDF)
* 💼 AI Career Coach
* 🎤 Interview Question Generator
* 🧠 Session Memory
* 🤖 Google Gemini Integration
* 🔀 Multi-Agent Architecture

---

## 🤖 AI Agents

### Resume Agent

* Extracts resume insights
* Evaluates resume quality
* Suggests improvements
* Calculates ATS score

### Career Agent

* Answers career-related questions
* Suggests learning roadmaps
* Recommends skills

### Interview Agent

* Generates interview questions
* Helps users prepare for technical interviews

### Manager Agent

* Routes user requests to the appropriate specialized AI agent.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* Google ADK
* PyPDF
* dotenv
* Git & GitHub

---

## 📂 Project Structure

```text
CareerPilot-AI/
│
├── agents/
├── adk/
├── memory/
├── services/
├── tools/
├── utils/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sejaljain23/CareerPilot-AI.git
```

Move into the project directory:

```bash
cd CareerPilot-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

* Students preparing for placements
* Fresh graduates
* Job seekers
* Career changers
* Professionals improving resumes

---

## 🔮 Future Improvements

* Job recommendation system
* LinkedIn profile analysis
* Mock interview with voice
* Resume keyword optimization
* Career progress dashboard
* Multi-language support

---

## 👩‍💻 Author

**Sejal Jain**

Developed as a capstone project for the Kaggle **5-Day AI Agents: Intensive Vibe Coding Course with Google**.

---

## 📄 License

This project is created for educational and portfolio purposes.

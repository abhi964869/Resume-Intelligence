import streamlit as st


def show():

    st.markdown(
        """
<div class="hero">

<div class="hero-title">

🚀 Resume Intelligence

</div>

<div class="hero-subtitle">

Your AI-powered career platform for Resume Analysis,
ATS Optimization,
Resume Rewriting,
Interview Preparation,
and Career Growth.

</div>

<div class="hero-chip">

Version 2.0

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    st.info(
        """
### 👋 Welcome to Resume Intelligence

Your all-in-one AI career assistant.

Use the sidebar to access:

- 📄 Resume Analysis
- 🤖 AI Review
- ✨ Resume Rewriter
- 💬 Resume Chat
- 🎯 Interview Preparation
- 📄 Cover Letter Generator
"""
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🤖 AI Review",
            "Ready",
        )

    with col2:
        st.metric(
            "💬 Resume Chat",
            "Ready",
        )

    with col3:
        st.metric(
            "✨ Resume Rewriter",
            "Ready",
        )

    with col4:
        st.metric(
            "🎯 Interview Prep",
            "Ready",
        )

    st.divider()

    st.subheader("⚡ Quick Actions")

left, right = st.columns(2)

with left:

    st.info("""
### 📄 Resume Analysis

Upload your resume and compare it with a job description.

➡️ Open **Resume** and **Analysis** from the sidebar.
""")

    st.info("""
### ✨ AI Resume Rewriter

Rewrite your resume for ATS optimization,
HR readability,
or international format.

➡️ Open **AI Resume Rewriter**.
""")

with right:

    st.info("""
### 🤖 AI Resume Review

Generate ATS review,
career roadmap,
cover letter,
and AI suggestions.

➡️ Open **AI Review**.
""")

    st.info("""
### 💬 Resume Chat

Ask questions about your resume,
career,
skills,
or interview preparation.

➡️ Open **Resume Chat**.
""")

    st.divider()

st.subheader("🚀 Platform Modules")

col1, col2 = st.columns(2)

with col1:

    st.success("📄 Resume Analysis")
    st.success("🤖 AI Resume Review")
    st.success("✨ Resume Rewriter")
    st.success("💬 Resume Chat")

with col2:

    st.success("🎯 Interview Preparation")
    st.success("📄 Cover Letter")
    st.success("🧭 Career Roadmap")
    st.success("📥 PDF Export")

row1 = st.columns(3)

with row1[0]:

    st.info("""
### 📄 Resume Analysis

✔ ATS Score

✔ Resume vs JD

✔ Missing Skills

✔ Resume Insights
""")

with row1[1]:

    st.info("""
### 🤖 AI Features

✔ Resume Review

✔ Career Roadmap

✔ Cover Letter

✔ AI Suggestions
""")

with row1[2]:

    st.info("""
### 💬 Smart Assistant

✔ Resume Chat

✔ Resume Rewriter

✔ Interview Prep

✔ PDF Export
""")

st.divider()

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.success("""
Python

Streamlit

Pandas
""")

with tech2:

    st.success("""
Gemini AI

Plotly

MySQL
""")

with tech3:

    st.success("""
Markdown

PDF Reports

Modern UI
""")
st.divider()

st.subheader("📊 Project Summary")

st.markdown("""
**Resume Intelligence** is an AI-powered platform that helps job seekers:

- Improve ATS compatibility
- Compare resumes with job descriptions
- Generate AI resume reviews
- Rewrite resumes professionally
- Prepare for interviews
- Generate cover letters
- Build personalized learning roadmaps
""")
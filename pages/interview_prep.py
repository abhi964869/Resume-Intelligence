import streamlit as st

from utils.gemini_ai import generate_interview_questions
from utils.pdf_report import create_pdf


def show():

    st.title("🎯 AI Interview Preparation")

    st.caption(
        "Generate interview questions based on your uploaded resume or job description."
    )

    resume = st.session_state.get("resume_text", "")
    jd = st.session_state.get("job_description_text", "")

    if not resume and not jd:
        st.warning("Please upload a Resume or Job Description first.")
        return

    role = st.selectbox(
        "Target Role",
        [
            "Data Analyst",
            "Python Developer",
            "Data Scientist",
            "Business Analyst",
            "DevOps Engineer",
            "Software Engineer",
        ],
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )

    if st.button(
        "🚀 Generate Interview Questions",
        use_container_width=True,
    ):

        with st.spinner("Generating interview questions..."):

            prompt = f"""
Target Role:
{role}

Difficulty:
{difficulty}

Resume:

{resume}

Job Description:

{jd}
"""

            questions = generate_interview_questions(prompt)

            st.session_state["interview_questions"] = questions

    if "interview_questions" in st.session_state:

        st.markdown(st.session_state["interview_questions"])

        pdf = create_pdf(
            st.session_state["interview_questions"]
        )

        st.download_button(
            "📄 Download Interview Questions",
            pdf,
            "Interview_Questions.pdf",
            "application/pdf",
            use_container_width=True,
        )
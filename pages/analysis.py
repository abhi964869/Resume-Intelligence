import streamlit as st

from utils.ats import (
    ats_score,
    matched_skills,
    missing_skills,
    generate_summary,
    recommend_improvements,
    interview_questions,
)


def show():
    st.title("📊 ATS Resume Analysis")

    resume_text = st.session_state.get("resume_text", "")
    jd_text = st.session_state.get("job_description_text", "")

    if not resume_text:
        st.warning("⚠️ Please upload your Resume first.")
        return

    if not jd_text:
        st.warning("⚠️ Please upload a Job Description first.")
        return

    st.success("✅ Resume and Job Description loaded successfully!")

    score = ats_score(resume_text, jd_text)

    st.subheader("🎯 ATS Score")
    st.progress(score / 100)
    st.metric("ATS Score", f"{score}%")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Skills")
        skills = matched_skills(resume_text, jd_text)

        if skills:
            for skill in skills:
                st.success(skill)
        else:
            st.info("No matched skills found.")

    with col2:
        st.subheader("❌ Missing Skills")
        missing = missing_skills(resume_text, jd_text)

        if missing:
            for skill in missing:
                st.error(skill)
        else:
            st.success("No missing skills.")

    st.divider()

    st.subheader("📄 Resume Summary")
    st.info(generate_summary(resume_text))

    st.divider()

    st.subheader("💡 Improvement Suggestions")

    for suggestion in recommend_improvements(resume_text, jd_text):
        st.write("•", suggestion)

    st.divider()

    st.subheader("🎤 Interview Questions")

    for i, question in enumerate(interview_questions(jd_text), start=1):
        st.write(f"{i}. {question}")

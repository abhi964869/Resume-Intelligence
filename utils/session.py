import streamlit as st


def initialize_session():
    defaults = {
        "resume_text": "",
        "job_description_text": "",
        "analysis": None,
        "ai_review": "",
        "improved_resume": "",
        "matched_skills": [],
        "missing_skills": [],
        "ats_score": 0,
        "active_page": "Dashboard",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
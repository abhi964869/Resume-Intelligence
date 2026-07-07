import streamlit as st
from utils.parser import extract_text

def show():
    st.title("📋 Job Description")

    st.write(
        "Upload a Job Description (PDF, DOCX, TXT) or paste it manually."
    )

    uploaded_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "docx", "txt"],
        key="jd_upload",
    )

    jd_text = ""

    if uploaded_file is not None:
        jd_text = extract_text(uploaded_file)

    st.markdown("### OR")

    manual_jd = st.text_area(
        "Paste Job Description",
        height=300,
        placeholder="Paste the complete job description here..."
    )

    if manual_jd.strip():
        jd_text = manual_jd

    if jd_text:
        st.session_state["job_description_text"] = jd_text

        st.success("✅ Job Description Loaded Successfully!")

        with st.expander("Preview", expanded=False):
            st.write(jd_text[:5000])

        st.metric(
            "Characters",
            len(jd_text)
        )
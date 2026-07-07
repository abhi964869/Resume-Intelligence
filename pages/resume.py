import streamlit as st
from utils.parser import extract_text


def show():
    st.title("📄 Resume Upload")

    st.markdown(
        "Upload your resume in **PDF**, **DOCX**, or **TXT** format."
    )

    uploaded_file = st.file_uploader(
        "Choose Resume",
        type=["pdf", "docx", "txt"],
        key="resume_upload",
    )

    if uploaded_file is not None:
        resume_text = extract_text(uploaded_file)

        st.session_state["resume_text"] = resume_text

        st.success("✅ Resume uploaded successfully!")

        st.subheader("Resume Preview")

        if resume_text:
            st.text_area(
                "Extracted Text",
                resume_text,
                height=350,
            )

            st.metric(
                "Characters Extracted",
                len(resume_text),
            )
        else:
            st.error("Could not extract text from the uploaded file.")
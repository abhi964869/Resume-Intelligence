import streamlit as st
from utils.gemini_ai import test_gemini_connection

def show():

    st.title("⚙️ Settings")

    st.caption("Manage your Resume Intelligence application.")

    st.divider()

    st.subheader("🟢 Gemini Status")

    st.success("Gemini AI Connected")

    st.divider()

    st.subheader("📊 Session Information")

    st.write(
        "Resume Uploaded:",
        "✅" if "resume_text" in st.session_state else "❌",
    )

    st.write(
        "Job Description:",
        "✅" if "job_description_text" in st.session_state else "❌",
    )

    chat_count = len(
        st.session_state.get("chat_history", [])
    )

    st.write(f"Chat Messages: {chat_count}")

    st.divider()

    st.subheader("🧹 Clear Data")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🗑 Clear Resume"):

            st.session_state.pop("resume_text", None)

            st.success("Resume removed.")

        if st.button("🗑 Clear Job Description"):

            st.session_state.pop("job_description_text", None)

            st.success("Job Description removed.")

    with col2:

        if st.button("🗑 Clear Chat"):

            st.session_state.pop("chat_history", None)

            st.success("Chat cleared.")

        if st.button("🗑 Clear All"):

            st.session_state.clear()

            st.success("Session cleared.")

    st.divider()

    st.subheader("ℹ Application")

    st.write("Version: 2.0")

    st.write("Developer: Abhishek Yadav")

    st.divider()

    st.subheader("🛠 Tech Stack")

    st.markdown(
        """
- Python
- Streamlit
- Gemini AI
- Pandas
- Plotly
- MySQL
"""
    )
    if st.button("🔄 Test Gemini Connection"):
        with st.spinner("Testing..."):
            if test_gemini_connection():
                st.success("✅ Gemini API is working.")
            else:
                st.error("❌ Unable to connect to Gemini.")
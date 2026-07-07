import streamlit as st


def show():

    st.markdown(
        """
<div class="hero">

<div class="hero-title">

🚀 Resume Intelligence

</div>

<div class="hero-subtitle">

AI-Powered Resume Optimization Platform

Built to help job seekers improve resumes,
increase ATS scores,
prepare for interviews,
and accelerate career growth.

</div>

<div class="hero-chip">

Version 2.0

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    st.subheader("✨ Core Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("📄 Resume Analysis")
        st.success("🤖 AI Resume Review")
        st.success("✨ Resume Rewriter")
        st.success("💬 Resume Chat")
        st.success("📄 Cover Letter")

    with col2:

        st.success("🎯 Interview Preparation")
        st.success("🧭 Career Roadmap")
        st.success("📊 ATS Optimization")
        st.success("📥 PDF Report Export")
        st.success("⚡ Interactive Dashboard")

    st.divider()

    st.subheader("🛠 Technology Stack")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.code(
            """
Python
Streamlit
Pandas
"""
        )

    with t2:
        st.code(
            """
Gemini AI
Plotly
MySQL
"""
        )

    with t3:
        st.code(
            """
Markdown
PDF Reports
Custom CSS
"""
        )

    st.divider()

    st.subheader("📊 Project Highlights")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Features", "10+")

    with c2:
        st.metric("AI Modules", "5")

    with c3:
        st.metric("Reports", "PDF")

    with c4:
        st.metric("Status", "Ready")

    st.divider()

    st.subheader("👨‍💻 Developer")

    st.info(
        """
**Abhishek Yadav**

AI | Data Analytics | Python | Streamlit

This project demonstrates practical use of
Generative AI, Resume Intelligence,
and interactive data applications.
"""
    )

    st.write("### 🔗 Connect")

    st.markdown(
        """
- GitHub: https://github.com/abhi964869

- LinkedIn: https://linkedin.com/in/abhishek-yadav-45570728a
"""
    )

    st.divider()

    st.caption(
        "Resume Intelligence • Version 2.0 • Built with ❤️ using Streamlit & Gemini AI"
    )
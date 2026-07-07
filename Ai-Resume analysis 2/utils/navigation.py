import streamlit as st
from pathlib import Path


def sidebar():
    logo = Path("assets/logo.png")

    with st.sidebar:

        if logo.exists():
            st.image(str(logo), width=80)

        st.title("Resume Intelligence")
        st.caption("AI Resume Analyzer")

        st.divider()

        page = st.radio(
            "Navigation",
            [
    "🏠 Dashboard",
    "📄 Resume",
    "📋 Job Description",
    "📊 Analysis",
    "🤖 AI Review",
    "✨ AI Resume Rewriter",
    "💬 Resume Chat",
    "🎯 Interview Prep",
    "⚙️ Settings",
    "ℹ️ About",
]
        )

        st.divider()

        st.markdown(
            """
            **Version 2.0**

            [GitHub](https://github.com/abhi964869)

            [LinkedIn](https://linkedin.com/in/abhishek-yadav-45570728a)
            """
        )

    return page
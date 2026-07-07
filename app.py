import streamlit as st

from utils.styles import load_css
from utils.navigation import sidebar

# Import Pages
from pages import resume
from pages import job_description
from pages import analysis
from pages import ai_review_pages
from pages import resume_chat
from pages import resume_rewriter

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Resume Intelligence",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------
# LOAD CSS
# ---------------------------

load_css()

# ---------------------------
# SIDEBAR
# ---------------------------

page = sidebar()

# ---------------------------
# PAGE ROUTING
# ---------------------------

if page == "🏠 Dashboard":

    from pages import dashboard

    dashboard.show()

elif page == "📄 Resume":

    resume.show()

elif page == "📋 Job Description":

    job_description.show()

elif page == "📊 Analysis":

    analysis.show()

elif page == "🤖 AI Review":

    ai_review_pages.show()

elif page == "✨ AI Resume Rewriter":

    resume_rewriter.show()
    
elif page == "💬 Resume Chat":

    resume_chat.show()

elif page == "🎯 Interview Prep":

    from pages import interview_prep

    interview_prep.show()


elif page == "⚙️ Settings":

    from pages import settings

    settings.show()


elif page == "ℹ️ About":

    from pages import about

    about.show()
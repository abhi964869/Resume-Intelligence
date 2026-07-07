import streamlit as st

from utils.gemini_ai import rewrite_resume
from utils.pdf_report import create_pdf
from utils.resume_parser import parse_resume_sections


def show():

    st.markdown(
    """
<div class="hero">

<div class="hero-title">

✨ AI Resume Rewriter

</div>

<div class="hero-subtitle">

Rewrite your resume using AI to improve
ATS score,
HR readability,
and recruiter appeal.

</div>

<div class="hero-chip">

Powered by Gemini AI

</div>

</div>
""",
    unsafe_allow_html=True,
)

    if "resume_text" not in st.session_state:
        st.warning("📄 Please upload your resume first.")
        return

    resume = st.session_state["resume_text"]
    st.write("")

    left, right = st.columns(2)

    with left:

        st.success("✅ Resume Uploaded")

    with right:

        st.info("🤖 AI Ready")

        st.subheader("🎯 Rewrite Style")
        # Persist the selected rewrite style in session state to ensure
        # it's available later (e.g. when clicking "Rewrite Again").
        st.selectbox(
            "Choose Rewrite Style",
            [
                "ATS Optimized",
                "HR Friendly",
                "International Resume",
                "Fresher Resume",
                "Senior Resume",
            ],
            key="rewrite_style",
        )

    # Ensure rewrite_style variable is defined outside the column context
    # by reading from session state with a sensible default.
    rewrite_style = st.session_state.get("rewrite_style", "ATS Optimized")

    st.write("")

    if st.button("🚀 Rewrite Resume with AI", use_container_width=True):
        with st.spinner("Rewriting your resume..."):
            rewritten_resume = rewrite_resume(resume, rewrite_style)
            st.session_state["rewritten_resume"] = rewritten_resume

if "rewritten_resume" in st.session_state:

    st.divider()

    # Ensure original resume text is available for display
    resume = st.session_state.get("resume_text", "")

    st.subheader("📄 Resume Comparison")

    original_col, ai_col = st.columns([1, 1])

    sections = parse_resume_sections(
        st.session_state["rewritten_resume"]
    )

    with original_col:

        st.markdown("### 📄 Original Resume")

        st.text_area(
            "Original Resume",
            resume,
            height=650,
            label_visibility="collapsed",
        )

    with ai_col:

        st.markdown("### ✨ AI Rewritten Resume")

        with st.expander(
            "📄 Professional Summary",
            expanded=True,
        ):
            st.markdown(
                sections.get(
                    "Professional Summary",
                    "Not Available",
                )
            )

        with st.expander("🛠 Skills"):
            st.markdown(
                sections.get(
                    "Skills",
                    "Not Available",
                )
            )

        with st.expander("🚀 Projects"):
            st.markdown(
                sections.get(
                    "Projects",
                    "Not Available",
                )
            )

        with st.expander("💼 Experience"):
            st.markdown(
                sections.get(
                    "Experience",
                    "Not Available",
                )
            )

        with st.expander("🎓 Education"):
            st.markdown(
                sections.get(
                    "Education",
                    "Not Available",
                )
            )

        with st.expander("🏆 Certifications"):
            st.markdown(
                sections.get(
                    "Certifications",
                    "Not Available",
                )
            )

    st.divider()

    st.subheader("⚡ Actions")

    b1, b2 = st.columns(2)

    pdf = create_pdf(
        st.session_state["rewritten_resume"]
    )

    with b1:

        st.download_button(
            "📄 Download Rewritten Resume",
            data=pdf,
            file_name="AI_Rewritten_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    with b2:
        if st.button(
            "🔄 Rewrite Again",
            use_container_width=True,
        ):

            with st.spinner("Rewriting resume..."):

                # Read rewrite style from session state here to avoid
                # NameError when this block runs outside the show() scope.
                current_style = st.session_state.get("rewrite_style", "ATS Optimized")

                rewritten_resume = rewrite_resume(
                    resume,
                    current_style,
                )

                st.session_state["rewritten_resume"] = rewritten_resume

            st.rerun()
            st.divider()

st.info(
    """
💡 **Tips for Best Results**

• Choose **ATS Optimized** when applying online.

• Choose **HR Friendly** for recruiter readability.

• Choose **International Resume** for global opportunities.

• Choose **Fresher Resume** if you have little or no work experience.

• Choose **Senior Resume** to emphasize leadership and measurable achievements.
"""
)
st.divider()

st.success(
    "✅ Resume rewriting completed successfully."
)

st.caption(
    "Review every section before downloading. AI suggestions should always be verified for accuracy."
)
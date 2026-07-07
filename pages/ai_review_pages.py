import streamlit as st

from utils.gemini_ai import (
    generate_resume_review,
    generate_learning_roadmap,
    generate_cover_letter,
    generate_interview_questions,
)

from utils.pdf_report import create_pdf


def show():

    st.markdown(
        """
<div class="hero">

<div class="hero-title">
🤖 AI Resume Review
</div>

<div class="hero-subtitle">
Generate AI-powered Resume Reviews,
Career Roadmaps,
Cover Letters,
and Interview Preparation.

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

    jd = st.session_state.get("job_description_text", "")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            "✅ Resume Uploaded"
        )

    with col2:

        if jd.strip():

            st.success(
                "📋 Job Description Loaded"
            )

        else:

            st.info(
                "📄 Resume-only Review Mode"
            )

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Resume Review",
            "🧭 Career Coach",
            "📄 Cover Letter",
            "🎤 Interview Prep",
        ]
    )

    # ==========================================================
    # TAB 1
    # ==========================================================

    with tab1:

        st.subheader("📊 AI Resume Analysis")

        st.caption(
            "Analyze your resume using Gemini AI."
        )

        if st.button(
            "✨ Generate AI Resume Review",
            use_container_width=True,
        ):

            with st.spinner(
                "Analyzing Resume..."
            ):

                if jd.strip():

                    review = generate_resume_review(
                        resume,
                        jd,
                    )

                else:

                    review = generate_resume_review(
                        resume,
                        """
No Job Description was provided.

Review this resume independently.

Generate:

1. ATS Score out of 100

2. Resume Summary

3. Strengths

4. Weaknesses

5. Missing Skills

6. Improvement Suggestions

7. Final Verdict
""",
                    )

                st.session_state[
                    "ai_review"
                ] = review

        if "ai_review" in st.session_state:

            with st.container(border=True):

                st.markdown(
                    st.session_state[
                        "ai_review"
                    ]
                )

            pdf = create_pdf(
                st.session_state[
                    "ai_review"
                ]
            )

            st.download_button(
                "📄 Download AI Report",
                data=pdf,
                file_name="AI_Resume_Report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    # ==========================================================
    # TAB 2
    # ==========================================================

    with tab2:

        st.subheader("🧭 AI Career Coach")

        st.caption(
            "Generate a personalized learning roadmap based on your resume and job description."
        )

        if st.button(
            "🚀 Generate Career Roadmap",
            use_container_width=True,
        ):

            with st.spinner(
                "Generating Career Roadmap..."
            ):

                roadmap = generate_learning_roadmap(
                    jd
                )

                st.session_state[
                    "career_roadmap"
                ] = roadmap

        if "career_roadmap" in st.session_state:

            with st.container(border=True):

                st.markdown(
                    st.session_state[
                        "career_roadmap"
                    ]
                )

            pdf = create_pdf(
                st.session_state[
                    "career_roadmap"
                ]
            )

            st.download_button(
                label="📄 Download Career Roadmap",
                data=pdf,
                file_name="Career_Roadmap.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="career_pdf",
            )

    # ==========================================================
    # TAB 3
    # ==========================================================

    with tab3:

        st.subheader("📄 AI Cover Letter")

        st.caption(
            "Generate a professional cover letter tailored to your resume and job description."
        )

        if st.button(
            "✨ Generate Cover Letter",
            use_container_width=True,
        ):

            with st.spinner(
                "Writing Cover Letter..."
            ):

                letter = generate_cover_letter(
                    resume,
                    jd,
                )

                st.session_state[
                    "cover_letter"
                ] = letter

        if "cover_letter" in st.session_state:

            with st.container(border=True):

                st.markdown(
                    st.session_state[
                        "cover_letter"
                    ]
                )

            pdf = create_pdf(
                st.session_state[
                    "cover_letter"
                ]
            )

            st.download_button(
                label="📄 Download Cover Letter",
                data=pdf,
                file_name="Cover_Letter.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="cover_pdf",
            )

       # ==========================================================
    # TAB 4
    # ==========================================================

    with tab4:

        st.subheader("🎤 AI Interview Preparation")

        st.caption(
            "Generate interview questions and model answers based on your resume or job description."
        )

        if st.button(
            "🎯 Generate Interview Questions",
            use_container_width=True,
        ):

            with st.spinner(
                "Preparing Interview Questions..."
            ):

                if jd.strip():

                    questions = generate_interview_questions(
                        jd
                    )

                else:

                    questions = generate_interview_questions(
                        """
No Job Description provided.

Generate interview questions
based on the uploaded resume.
"""
                    )

                st.session_state[
                    "interview_questions"
                ] = questions

        if "interview_questions" in st.session_state:

            with st.container(border=True):

                st.markdown(
                    st.session_state[
                        "interview_questions"
                    ]
                )

            pdf = create_pdf(
                st.session_state[
                    "interview_questions"
                ]
            )

            st.download_button(
                label="📄 Download Interview Questions",
                data=pdf,
                file_name="Interview_Questions.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="interview_pdf",
            )

    st.divider()

    st.info(
        """
💡 **Tip**

For the best AI results, upload **both your Resume and the Job Description**.
If you don't have a Job Description yet, Resume-only mode is fully supported.
"""
    )
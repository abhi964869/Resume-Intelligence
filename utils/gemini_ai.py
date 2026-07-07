import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv(override=True)

client = None


def get_client(api_key=None):
    """
    Returns a Gemini client using either:
    1. API key passed to the function
    2. GEMINI_API_KEY from .env
    """

    global client

    # Reload .env every call
    load_dotenv(override=True)

    key = api_key if api_key else os.getenv("GEMINI_API_KEY")

    if not key:
        raise ValueError(
            "GEMINI_API_KEY not found. Please add it to your .env file."
        )

    if client is None:
        client = genai.Client(api_key=key)

    return client


def ask_gemini(prompt: str, api_key=None):
    """
    Sends a prompt to Gemini and returns the response.
    """

    try:
        client = get_client(api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"❌ Gemini Error:\n\n{str(e)}"


# ---------------------------------------------------
# AI Resume Review
# ---------------------------------------------------

def generate_resume_review(resume_text, jd_text, api_key=None):

    prompt = f"""
You are an expert ATS recruiter.

Analyze the following Resume against the Job Description.

Resume:
{resume_text}

Job Description:
{jd_text}

Generate a professional report with:

# ATS Score (/100)

# Resume Strengths

# Resume Weaknesses

# Missing Skills

# Resume Improvements

# Overall Feedback

# Final Verdict
"""

    return ask_gemini(prompt, api_key)


# ---------------------------------------------------
# Career Roadmap
# ---------------------------------------------------

def generate_learning_roadmap(resume_text, jd_text, rewrite_style, api_key=None):

    prompt = f"""
You are a world-class resume writer, ATS optimization expert, HR recruiter, and career coach.

Your task is to rewrite the user's resume according to the selected rewrite style.

Rewrite Style:
{rewrite_style}

IMPORTANT RULES:

- Never invent work experience.
- Never invent projects.
- Never invent certifications.
- Never invent skills.
- Never change factual information.
- Improve grammar and sentence structure.
- Improve readability.
- Improve ATS compatibility.
- Use strong action verbs.
- Quantify achievements wherever possible.
- Make the resume modern and professional.
- Keep the resume concise.
- Preserve all factual information.

Resume:

{resume_text}

========================================================

Return ONLY the rewritten resume.

Return it in EXACTLY this Markdown structure.

# Professional Summary

...

# Skills

...

# Projects

...

# Experience

...

# Education

...

# Certifications

...

========================================================

Rules:

- Do NOT add extra headings.
- Do NOT write explanations.
- Do NOT say "Here is your rewritten resume."
- Do NOT use tables.
- Keep clean Markdown.
- If a section is missing in the original resume, write "Not Available".
"""

    return ask_gemini(prompt, api_key)


# ---------------------------------------------------
# Interview Questions
# ---------------------------------------------------

def generate_interview_questions(jd_text, api_key=None):

    prompt = f"""
Generate interview questions based on this Job Description.

{jd_text}

Include:

• HR Questions
• Technical Questions
• Coding Questions
• Model Answers
"""

    return ask_gemini(prompt, api_key)


# ---------------------------------------------------
# Cover Letter
# ---------------------------------------------------

def generate_cover_letter(resume_text, jd_text, api_key=None):

    prompt = f"""
Write a professional cover letter.

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    return ask_gemini(prompt, api_key=api_key)
def rewrite_resume(
    resume_text,
    rewrite_style,
    api_key: str | None = None,
):

    prompt = f"""
You are a professional resume writer,
ATS expert,
and recruiter.

Rewrite the following resume.

Rewrite Style:

{rewrite_style}

Rules:

- Never invent experience.
- Never invent projects.
- Never invent skills.
- Improve grammar.
- Improve readability.
- Improve ATS compatibility.
- Use stronger action verbs.
- Quantify achievements wherever possible.
- Preserve factual information.
- Return clean Markdown.

Resume:

{resume_text}
"""

    return ask_gemini(
        prompt,
        api_key=api_key,
    )
def test_gemini_connection(api_key=None):
    """
    Returns True if Gemini is reachable.
    """

    try:

        response = ask_gemini(
            "Reply with exactly the word OK.",
            api_key=api_key,
        )

        return response.strip().upper() == "OK"

    except Exception:

        return False
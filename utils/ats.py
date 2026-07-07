import re

SKILLS = [
    "python",
    "sql",
    "mysql",
    "postgresql",
    "excel",
    "power bi",
    "tableau",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "statistics",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "linux",
    "git",
    "github",
    "jenkins",
    "terraform",
    "ansible",
    "mongodb",
    "streamlit",
    "flask",
    "django",
    "fastapi",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "communication",
    "problem solving",
    "teamwork"
]


def clean(text):
    if text is None:
        return ""
    return text.lower()


def extract_skills(text):
    text = clean(text)

    found = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)

    return sorted(list(set(found)))


def matched_skills(resume_text, jd_text):
    resume = set(extract_skills(resume_text))
    jd = set(extract_skills(jd_text))
    return sorted(list(resume & jd))


def missing_skills(resume_text, jd_text):
    resume = set(extract_skills(resume_text))
    jd = set(extract_skills(jd_text))
    return sorted(list(jd - resume))


def ats_score(resume_text, jd_text):
    jd = extract_skills(jd_text)

    if len(jd) == 0:
        return 0

    matched = matched_skills(resume_text, jd_text)

    score = round((len(matched) / len(jd)) * 100)

    return min(score, 100)


def generate_summary(resume_text):
    skills = extract_skills(resume_text)

    if len(skills) == 0:
        return "No technical skills were detected in the resume."

    return (
        f"The resume contains {len(skills)} recognized technical skills. "
        "The candidate appears suitable for technical roles based on the detected skills."
    )


def recommend_improvements(resume_text, jd_text):
    missing = missing_skills(resume_text, jd_text)

    suggestions = []

    if missing:
        suggestions.append(
            "Add the missing technical skills if you have experience with them."
        )

    suggestions.append(
        "Quantify your achievements using numbers and percentages."
    )

    suggestions.append(
        "Use ATS-friendly section headings."
    )

    suggestions.append(
        "Keep the resume to one page."
    )

    suggestions.append(
        "Customize your resume for each job description."
    )

    return suggestions


def interview_questions(jd_text):

    skills = extract_skills(jd_text)

    questions = []

    for skill in skills[:10]:
        questions.append(
            f"Explain your experience with {skill}."
        )

    if len(questions) == 0:
        questions = [
            "Tell me about yourself.",
            "Describe one challenging project.",
            "Why should we hire you?"
        ]

    return questions
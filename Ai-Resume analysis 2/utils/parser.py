import re
from PyPDF2 import PdfReader
from docx import Document


def extract_pdf(file):
    text = ""

    try:
        pdf = PdfReader(file)

        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    except Exception:
        return ""

    return clean_text(text)


def extract_docx(file):
    text = ""

    try:
        doc = Document(file)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception:
        return ""

    return clean_text(text)


def extract_txt(file):
    try:
        return clean_text(file.read().decode("utf-8"))
    except Exception:
        return ""


def extract_text(file):
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_pdf(file)

    elif filename.endswith(".docx"):
        return extract_docx(file)

    elif filename.endswith(".txt"):
        return extract_txt(file)

    return ""


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()
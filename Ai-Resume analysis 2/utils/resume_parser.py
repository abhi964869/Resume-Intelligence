import re


def parse_resume_sections(markdown_text):
    """
    Parse AI rewritten resume into sections.
    """

    section_names = [
        "Professional Summary",
        "Skills",
        "Projects",
        "Experience",
        "Education",
        "Certifications",
    ]

    sections = {}

    for i, section in enumerate(section_names):

        current_heading = rf"#\s*{re.escape(section)}"

        current_match = re.search(current_heading, markdown_text)

        if not current_match:
            sections[section] = "Not Available"
            continue

        start = current_match.end()

        if i < len(section_names) - 1:

            next_heading = rf"#\s*{re.escape(section_names[i + 1])}"

            next_match = re.search(next_heading, markdown_text)

            if next_match:
                end = next_match.start()
            else:
                end = len(markdown_text)

        else:

            end = len(markdown_text)

        sections[section] = markdown_text[start:end].strip()

    return sections
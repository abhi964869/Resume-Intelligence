from io import BytesIO

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = HexColor("#1F4E79")

heading_style = styles["Heading2"]
heading_style.textColor = HexColor("#1565C0")

normal_style = styles["BodyText"]


def create_pdf(ai_review):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    story = []

    story.append(
        Paragraph(
            "AI Resume Intelligence Report",
            title_style,
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "AI Resume Review",
            heading_style,
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            ai_review.replace("\n", "<br/>"),
            normal_style,
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
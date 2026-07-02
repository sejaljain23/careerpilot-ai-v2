from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_report(filename, analysis, ats_score):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>CareerPilot AI Resume Report</b>", styles["Title"]))
    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}/100", styles["Heading2"]))
    story.append(Paragraph(analysis.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)
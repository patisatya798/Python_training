from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(text, filename="report.pdf"):
    pdf = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    for line in text.split("\n"):
        content.append(Paragraph(line, styles["Normal"]))

    pdf.build(content)

    print(" PDF created!")
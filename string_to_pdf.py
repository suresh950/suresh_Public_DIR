from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Your long string
text = """
This is a long paragraph of text that will automatically wrap inside the PDF.
It will respect margins and if it becomes too big for one page, ReportLab
will continue it on the next page without cutting words.
You can add as much text as you want here, and it will handle page breaks.
"""

# Create PDF with margins: left, right, top, bottom = 50px
pdf_file = "wrapped_output.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        leftMargin=50, rightMargin=50,
                        topMargin=50, bottomMargin=50)

# Get default style
styles = getSampleStyleSheet()
style = styles["Normal"]  # You can also use "BodyText"

# Create Paragraph object (handles wrapping + multi-page)
story = []
story.append(Paragraph(text, style))
story.append(Spacer(1, 12))  # Add a little spacing

# Build PDF
doc.build(story)

print(f"PDF created: {pdf_file}")


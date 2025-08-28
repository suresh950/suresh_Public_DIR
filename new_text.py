from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Your multi-line string
text = """This is line one.
This is line two.
This is line three, and it should appear on the next line in the PDF."""

# Convert newlines to <br/> so Paragraph respects them
formatted_text = text.replace("\n", "<br/>")

# Create PDF with margins
pdf_file = "multiline_output.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        leftMargin=50, rightMargin=50,
                        topMargin=50, bottomMargin=50)

# Styles
styles = getSampleStyleSheet()
style = styles["Normal"]

# Add text as a Paragraph (with line breaks preserved)
story = [Paragraph(formatted_text, style), Spacer(1, 12)]

# Build the PDF
doc.build(story)

print(f"PDF created: {pdf_file}")

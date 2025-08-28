from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Example text
text = """This is line one.\nThis is line two.
/nThis is line three.
This is line four."""

# Replace both "\n" and "/n" with <br/>
formatted_text = text.replace("\n", "<br/>").replace("/n", "<br/>")

# Create PDF with margins
pdf_file = "multiline_output.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        leftMargin=50, rightMargin=50,
                        topMargin=50, bottomMargin=50)

# Style
styles = getSampleStyleSheet()
style = styles["Normal"]

# Add to PDF
story = [Paragraph(formatted_text, style), Spacer(1, 12)]
doc.build(story)

print(f"PDF created: {pdf_file}")

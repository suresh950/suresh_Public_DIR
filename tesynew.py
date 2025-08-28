from reportlab.platypus import SimpleDocTemplate, Paragraph
          from reportlab.lib.pagesizes import A4
          from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
          import re
          import os
      
          output_file = "job_output.txt"
          pdf_file = "job_output.pdf"
          
          with open("job_output.txt", "r") as file:
              job_output = file.read()

          cleaned_output = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', job_output)
          
          with open("updated_job_output.txt", "a") as f:
              f.write(cleaned_output)

      
          # Define margins (in points; 1 inch = 72 points)
          left_margin = 20
          right_margin = 20
      
          # Create PDF document with margins
          doc = SimpleDocTemplate(
              pdf_file,
              pagesize=A4,
              leftMargin=left_margin,
              rightMargin=right_margin,
              topMargin=20,
              bottomMargin=20
          )
      
          # Define a small font style
          styles = getSampleStyleSheet()
          small_style = ParagraphStyle(
              'Small',
              parent=styles['Normal'],
              fontSize=8,         # smaller font
              leading=10          # line spacing
          )
      
          elements = []
      
          if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
              elements.append(Paragraph("No output from Ansible playbook.", small_style))
          else:
              with open(output_file) as f:
                  for line in f:
                      line = line.strip()
                      if line:
                          elements.append(Paragraph(line, small_style))
      
          doc.build(elements)

#!/usr/bin/env python3
"""Convert task_4_1_report.md to report.pdf using FPDF"""

import subprocess
import sys

# Install FPDF2 if not present
try:
    from fpdf import FPDF
except ImportError:
    print("Installing fpdf2...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "fpdf2"])
    from fpdf import FPDF

# Read the markdown file
with open('partB/task_4_1_report.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Create PDF
class ReportPDF(FPDF):
    def header(self):
        pass
    
    def footer(self):
        self.set_y(-0.75)
        self.set_font("Arial", "I", 9)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

# Initialize PDF
pdf = ReportPDF('P', 'in', 'Letter')
pdf.set_margins(1, 0.75, 1)
pdf.add_page()

# Set initial font
pdf.set_font("Times", "", 10)

# Process markdown line by line
lines = content.split('\n')
for line in lines:
    line = line.rstrip()
    
    if not line:
        # Empty line - add spacing
        pdf.ln(4)
    elif line.startswith('# '):
        # Title
        pdf.set_font("Times", "B", 14)
        pdf.multi_cell(0, 10, line[2:].strip())
        pdf.set_font("Times", "", 10)
        pdf.ln(3)
    elif line.startswith('## '):
        # Section heading
        pdf.set_font("Times", "B", 11)
        pdf.ln(2)
        pdf.multi_cell(0, 10, line[3:].strip())
        pdf.set_font("Times", "", 10)
        pdf.ln(2)
    elif line.startswith('### '):
        # Subsection
        pdf.set_font("Times", "B", 10)
        pdf.ln(2)
        pdf.multi_cell(0, 10, line[4:].strip())
        pdf.set_font("Times", "", 10)
        pdf.ln(1)
    elif line.startswith('---'):
        # Horizontal rule
        y = pdf.get_y()
        pdf.set_draw_color(200, 200, 200)
        pdf.line(1, y + 3, 7.5, y + 3)
        pdf.set_draw_color(0, 0, 0)
        pdf.ln(5)
    elif line.startswith('|'):
        # Skip table markers (simplified - just show as text)
        continue
    elif line.startswith('- '):
        # Bullet point
        pdf.set_font("Times", "", 9)
        pdf.multi_cell(0, 8, line[2:].strip(), new_x="LMARGIN")
        pdf.set_font("Times", "", 10)
    elif line[0:2].isdigit() and len(line) > 2 and line[2] == '.':
        # Numbered list
        pdf.set_font("Times", "", 9)
        pdf.multi_cell(0, 8, line, new_x="LMARGIN")
        pdf.set_font("Times", "", 10)
    else:
        # Regular text
        if line.strip():
            pdf.set_font("Times", "", 10)
            # Handle bold/italic markup
            text = line.strip()
            text = text.replace('**', '')
            pdf.multi_cell(0, 6, text)

# Save PDF
pdf.output('partB/report.pdf')

import os
size = os.path.getsize('partB/report.pdf')
print(f"✅ PDF created: partB/report.pdf ({size} bytes)")

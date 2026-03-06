#!/usr/bin/env python3
"""Convert task_4_1_report.md to report.pdf"""

import subprocess
import sys

# Install required packages
try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "markdown"])

try:
    from weasyprint import HTML
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "weasyprint"])

import markdown
from weasyprint import HTML

# Read markdown file
with open('partB/task_4_1_report.md', 'r') as f:
    md_content = f.read()

# Convert markdown to HTML with table extension
html_content = markdown.markdown(md_content, extensions=['tables'])

# Create full HTML with styling
full_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            margin: 1in;
            size: letter;
        }
        body {
            font-family: "Times New Roman", serif;
            font-size: 10pt;
            line-height: 1.5;
            color: #000;
        }
        h1 {
            font-size: 14pt;
            font-weight: bold;
            margin-top: 0;
            margin-bottom: 12pt;
            page-break-after: avoid;
        }
        h2 {
            font-size: 11pt;
            font-weight: bold;
            margin-top: 14pt;
            margin-bottom: 8pt;
            page-break-after: avoid;
        }
        h3 {
            font-size: 10pt;
            font-weight: bold;
            margin-top: 10pt;
            margin-bottom: 6pt;
            page-break-after: avoid;
        }
        p {
            margin: 0 0 8pt 0;
            text-align: justify;
        }
        ul, ol {
            margin: 8pt 0;
            padding-left: 24pt;
        }
        li {
            margin-bottom: 4pt;
            font-size: 10pt;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 12pt 0;
            font-size: 9pt;
        }
        thead {
            background-color: #e8e8e8;
        }
        th {
            border: 1px solid #999;
            padding: 6pt 4pt;
            text-align: left;
            font-weight: bold;
        }
        td {
            border: 1px solid #ccc;
            padding: 4pt;
        }
        hr {
            border: none;
            border-top: 1px solid #ccc;
            margin: 10pt 0;
        }
        strong {
            font-weight: bold;
        }
        em {
            font-style: italic;
        }
    </style>
</head>
<body>
""" + html_content + """
</body>
</html>
"""

# Generate PDF
try:
    HTML(string=full_html).write_pdf('partB/report.pdf')
    
    import os
    size = os.path.getsize('partB/report.pdf')
    print(f"✅ PDF successfully created: partB/report.pdf ({size} bytes)")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

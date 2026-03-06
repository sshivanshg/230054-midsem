#!/usr/bin/env python3
import sys

try:
    import pdfplumber
    with pdfplumber.open('MidSem_PartB.pdf') as pdf:
        print(f"Total pages: {len(pdf.pages)}\n")
        for i, page in enumerate(pdf.pages):
            print(f"\n{'='*60}")
            print(f"PAGE {i+1}")
            print('='*60)
            text = page.extract_text()
            if text:
                print(text)
            else:
                print("(No extractable text)")
except ImportError:
    print("pdfplumber not installed, trying PyPDF2")
    try:
        from PyPDF2 import PdfReader
        with open('MidSem_PartB.pdf', 'rb') as f:
            reader = PdfReader(f)
            print(f"Total pages: {len(reader.pages)}\n")
            for i in range(len(reader.pages)):
                print(f"\n{'='*60}")
                print(f"PAGE {i+1}")
                print('='*60)
                text = reader.pages[i].extract_text()
                if text:
                    print(text)
                else:
                    print("(No extractable text)")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

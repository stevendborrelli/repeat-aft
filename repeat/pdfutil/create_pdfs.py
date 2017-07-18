#!/usr/bin/env nix-shell

# Put this line below the above to have nix install reportlab:
# !nix-shell -i python3 -p python3Packages.reportlab
"""
Create both a blank PDF file for testing purposes, and one with just a little
text. Execute directly (e.g. `./create_pdf.py`) to allow Nix to fetch
ReportLab.
"""

from reportlab.pdfgen import canvas

# Blank PDF
c = canvas.Canvas("blank.pdf")
c.showPage()
c.save()

c = canvas.Canvas("lorem.pdf")
c.drawString(100, 100,
             "Lorem Ipsum is the dummy text of the typesetting industry.")
c.showPage()
c.save()

from PyPDF2 import pdfFileWriter
from pathlib import Path

pdf_writer = pdfFileWriter()

page = pdf_writer.addBlankpage(width = 72, height = 72)

with Path("blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


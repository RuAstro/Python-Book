from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

pdf_path = (
    Path.home()  / "Desktop" / "Python BOOK" / "code" / "Chapter_14" / "Pride_and_Prejudice.pdf"
)
input_pdf = PdfReader(str(pdf_path))

pdf_writer = PdfWriter()
for n in range(1, 4):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)
    
pdf_writer.getNumPages()

with Path("chapter1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
    
pdf_writer = PdfWriter()

for page in input_pdf.pages[1:4]:
    pdf_writer.addPage(page)
    
with Path("chapter1_slice.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
    
pdf_writer = PdfWriter()
pdf_writer.appendPagesFromReader(PdfReader)
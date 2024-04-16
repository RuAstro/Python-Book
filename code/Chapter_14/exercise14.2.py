from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf = Path.home() / "Pride_and_Prejudice.pdf"

Pdf_reader = PdfReader(str(pdf))

last_page = Pdf_reader.reader[-1]

pdf_writer = pdf_writer()
pdf_writer.addPage()

output_path = Path.home() / "last_page.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
    
#need to do number 2


first_half_writer = PdfWriter
second_half_writer = PdfWriter

first_half_pages = Pdf_reader.pages[0:150]
second_half_pages = Pdf_reader.pages[150:]

for page in first_half_pages:
    first_half_writer.addPage(page)
    
for page in second_half_pages:
    second_half_writer.addPage(page)

first_half_output_path = Path.home() / "first_half.pdf"
with first_half_output_path.open(mode="wb") as output_file:
    first_half_writer.write(first_half_output_path)
    

second_half_output_path = Path.home() / "second_half.pdf"
with second_half_output_path.open(mode="wb") as output_file:
    second_half_writer.write(second_half_output_path)

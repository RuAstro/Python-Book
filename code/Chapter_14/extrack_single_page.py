from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.home() / "Users" / "User" / "Home" / "Desktop" / "Python BOOK" / "code" / "Chapter_14" / "Pride_and_Prejudice.pdf"
)

input = PdfFileReader(str(pdf_path))

first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addpage(first_page)

with Path("first_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
    
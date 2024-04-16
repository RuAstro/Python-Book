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
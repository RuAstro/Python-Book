from pathlib import Path
from PyPDF2 import PdfReader
pdf = Path.cwd()
pdf = Path.cwd() / "code" / "Chapter_14" / "zen.pdf"

pdf_reader = PdfReader(str(pdf))

num_pages = pdf_reader.getNumPages()
print(num_pages)


first_page = pdf_reader.getPage()

text = first_page.text()

print(text)
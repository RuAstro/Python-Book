from pathlib import Path
from PyPDF2 import pdfFileReader

pdf = Path.cwd() / "user" / "zen.pdf"

pdf_reader = pdfFileReader(str(pdf))

num_pages = pdf_reader.getNumPages()
print(num_pages)


first_page = pdf_reader.getPage()

text = first_page.text()

print(text)
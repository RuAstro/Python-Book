from PyPDF2 import PdfFileReader

from pathlib import Path

pdf_path = (
    Path.home() / "Desktop" / "Python BOOK" / "code" / "Chapter_14" / "Pride_and_Prejudice.pdf"
)
pdf = PdfFileReader(str(pdf_path))


pdf.getNumPages()

#to get document information
pdf.documentInfo

#to get the title
pdf.documentInfo.title

first_page = pdf.getPage(0)

type(first_page)

#you can extract the pages text with PageObject.extractText():
first_page.extractText()

#the for loops prints the text from every page in the pdf
for page in pdf.pages:
    print(page.extractText())
    
from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = (
    Path.home() / "Desktop" / "Python BOOK" / "code" / "Chapter 14" / "Pride_and_Prejudice.pdf"
)
pdf = PdfFileReader(str(pdf_path))


# pdf.getNumPages()

#to get document information
#pdf.documentInfo

#to get the title
#pdf.documentInfo.title
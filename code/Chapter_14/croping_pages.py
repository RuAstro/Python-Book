from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import copy

pdf_path = (
    Path.home()
    / "python-basics-exercises"
    / "ch14-interact-with-pdf-files"
    / "practice_files"
    / "half_and_half.pdf"
)

# create a new PdfFileReader object and get the first page of the PDF:
pdf_reader = PdfReader(str(pdf_path))
first_page = pdf_reader.getPage(0)


# PageObject instances like first_page have a .mediaBox attribute that represents a rectangular area defining the boundaries of the page
first_page.mediaBox
RectangleObject([0, 0, 792, 612])

first_page.mediaBox.lower_left = (0, 480)

first_page.mediaBox.lower_right

first_page.mediaBox.upper_left

first_page.mediaBox.upper_right

# writing cropped page to new PDF file:
pdf_writer = PdfWriter()
pdf_writer.addPage(first_page)
with Path("cropped_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

first_page = pdf_reader.getPage(0)
left_side = copy.deepcopy(first_page)

current_coords = left_side.mediaBox.upperRight
new_coords = (current_coords[0] / 2, current_coords[1])
left_side.mediaBox.upperRight = new_coords

# get copy of first page:
right_side = copy.deepcopy(first_page)

# move upperLeft corner instead of the upperRight corner:
right_side.mediaBox.upperLeft = new_coords

# add the left_side and right_side pages to pdf_writer and write them to a new PDF file:
pdf_writer.addPage(left_side)
pdf_writer.addPage(right_side)
with Path("cropped_pages.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

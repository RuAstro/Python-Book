from PyPDF2 import PdfReader, PdfWriter

# Open the scrambled PDF
with open("chapter_14/scrambled.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = pdf_reader.numPages

# Create a list to store page numbers and their rotation angles
pages_info = []

# Extract page numbers and rotation angles
for page_num in range(num_pages):
    page = pdf_reader.getPage(page_num)
    page_number = int(page.extractText())
    rotation_angle = int(page.get("/Rotate", 0))
    pages_info.append(page_num, page_number, rotation_angle)

# sort pages based on their page numbers
pages_info.sort(key=lambda x: x[1])

# Create a new PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Iterate through the sorted pages, add them to new PDF
for page_info in pages_info:
    page_num, rotation_angle = page_info
    page = pdf_reader.getPage(page_num)

    # Rotate page if needed
    if rotation_angle != 0:
        page.rotate(rotation_angle)

        pdf_writer.addPage(page)
    # Write the unscrambled PDF to a new file
    with open("unscrambled.pdf", "wb") as output_file:
        pdf_writer.write(output_file)

print("PDF Unscrambled is saved")

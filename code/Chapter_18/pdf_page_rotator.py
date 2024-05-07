from email.policy import default
import easygui as gui
from PyPDF2 import PdfReader, PdfWriter

input_path = gui.fileopenbox(title="Select a PDF to rotate...", default="*.pdf")

if input_path is None:
    exit()

choices = ("90", "180", "270")
degrees = gui.buttonbox(
    msg="Rotate the PDF clockwise by how many degrees?",
    title="Choose rotation...",
    choices=choices,
)

save_title = "Save the rotated PDF as..."
file_type = "*.pdf"
output_path = gui.filesavebox(title=save_title, default=file_type)

while input_path == output_path:

    gui.msgbox(msg - "Cannot overwrite original file")

    output_file = gui.filesavebox(title=save_title, default=file_type)

if output_path is None:
    exit()

input_file = PdfReader(input_path)
output_pdf = PdfWriter()

for page in input_file.pages:
    page = page.rotate(int(degrees))
    output_pdf.add_page(page)

with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)

from email.policy import default
import easygui as gui
from PyPDF2 import PdfReader, PdfWriter

# 1. Display a file selection dialog for opening a PDF file.
input_path = gui.fileopenbox(title="Select a PDF to rotate...", default="*.pdf")

# 2. If the user cancels the dialog, then exit the program.
if input_path is None:
    exit()

# 3. Ask the user to select one of 90, 180, or 270 degrees.
choices = ("90", "180", "270")
degrees = gui.buttonbox(
    msg="Rotate the PDF clockwise by how many degrees?",
    title="Choose rotation...",
    choices=choices,
)

# 4. Display a file selection dialog for saving the rotated PDF.
save_title = "Save the rotated PDF as..."
file_type = "*.pdf"
output_path = gui.filesavebox(title=save_title, default=file_type)

# 5. If the user tries to save with the same name as the input file:
while input_path == output_path:

    gui.msgbox(msg - "Cannot overwrite original file")

    output_file = gui.filesavebox(title=save_title, default=file_type)

# 6. If the user cancels the file save dialog, then exit the program.
if output_path is None:
    exit()

# 7. Perform the page rotation:
# - Open the selected PDF.
input_file = PdfReader(input_path)
output_pdf = PdfWriter()

# - Rotate all the pages.
for page in input_file.pages:
    page = page.rotate(int(degrees))
    output_pdf.add_page(page)

# - Save the rotated PDF to the selected file.
with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)

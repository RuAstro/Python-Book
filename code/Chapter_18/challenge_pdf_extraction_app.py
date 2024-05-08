import PyPDF2
import easygui as gui
from PyPDF2 import PdfReader, PdfWriter


def extract_pages(pdf_file, start_page, end_page, save_path):
    # Open the PDF file
    pdf = open(pdf_file, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf)

    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Extract pages from start_page to end_page
    for page_num in range(start_page - 1, end_page):
        pdf_writer.addPage(pdf_reader.getPage(page_num))

    # Write the extracted pages to a new PDF file
    with open(save_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    pdf.close()


def main():
    # Ask the user to select a PDF file
    pdf_file = gui.fileopenbox(msg="Select a PDF file to open", filetypes=["*.pdf"])
    if pdf_file is None:
        gui.msgbox("No PDF file chosen. Exiting program.")
        return

    #  Ask for a starting page number
    while True:
        start_page = gui.integerbox("Enter the starting page number")
        if start_page is None:
            gui.msgbox("No starting page number entered. Exiting program.")
            return
        elif start_page <= 0:
            gui.msgbox("Invalid starting page number. Please enter a positive integer.")
        else:
            break

    #  Ask for an ending page number
    while True:
        end_page = gui.integerbox("Enter the ending page number")
        if end_page is None:
            gui.msgbox("No ending page number entered. Exiting program.")
            return
        elif end_page <= 0:
            gui.msgbox("Invalid ending page number. Please enter a positive integer.")
        elif end_page < start_page:
            gui.msgbox("Ending page number cannot be less than starting page number.")
        else:
            break

    # Ask for the location to save the extracted pages
    while True:
        save_path = gui.filesavebox(
            msg="Select a location to save the extracted pages",
            default="output.pdf",
            file_types=["*.pdf"],
        )
        if save_path is None:
            gui.msgbox("No save location selected. Exiting program.")
            return
        elif save_path == pdf_file:
            gui.msgbox(
                "You can't overwrite the input file. Please choose a different save location."
            )
        else:
            break

    # Extract pages and save to the selected location
    extract_pages(pdf_file, start_page, end_page, save_path)
    gui.msgbox(
        f"Pages {start_page} to {end_page} extracted successfully and saved to {save_path}"
    )


if __name__ == "__main__":
    main()

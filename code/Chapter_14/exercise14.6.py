from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# for opening pdf file
with open("chapter_14_practice_files/top_secret.pdf", "rb") as file:
    reader = PdfReader(file)
    writer = PdfWriter()

    # Copy each page to the writer object
    for page in reader.pages:
        writer.add_page(page)

    # Encrypt the pdf with the user password...
    writer.encrypt(user_pwd="Unguessable")

    # Write encrypted pdf to new file...
    with open("top_secret_encrypted.pdf") as output_file:
        writer.write(output_file)

    # check if the pdf is encrypted
    if reader.is_encrypted:

        if reader.decrypt("Unguessable"):
            # get text from first page.
            first_page_text = reader.pages[0].extract_text()
            print("Text from the first page:")
            print(first_page_text)

        else:
            print("Failed")

    else:
        print("PDF NOT encrypted.")

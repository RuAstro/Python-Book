from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader

merger = PdfMerger()

# Concatenate merge1.pdf and merge2.pdf
merger.append("chapter_14_practice_files/merge1.pdf")
merger.append("chapter_14_practice_files/merge2.pdf")
merger.write("concatenated.pdf")
merger.close()

# Merge merge3.pdf between the two pages in concatenated.pdf
merger = PdfMerger()
merger.append("concatenated.pdf")
merger.merge(1, "chapter_14_practice_files/merge3.pdf")
merger.write("merged.pdf")
merger.close()

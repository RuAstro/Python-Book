from pathlib import Path
from PyPDF2 import PdfMerger

report_dir = (
    Path.home() / 
    "ch14-interact-with-pdf-files" /
    "practice_files" 
    "quarterly_report"
)

report_path = report_dir / "report.pdf"
toc_path = report_dir / "toc.pdf"

# append the report PDF to a new PdfFileMerger instance using .append():
pdf_merger = PdfMerger()
pdf_merger.append(str(report_path))

#Every page in the table of contents PDF is inserted before the page
#at index 1. Since the table of contents PDF is only one page, it gets
#inserted at index 1. The page currently at index 1 then gets shifted to
#index 2.
pdf_merger.merge(1, str(toc_path))

#the merged PDF to an output file:
with Path("full_report.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
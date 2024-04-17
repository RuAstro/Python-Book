from PyPDF2 import PdfMerger
from pathlib import Path

pdf_merger = PdfMerger()
reports_dir = (
    Path.home() / 
    "python-basics-exercises" /
    "ch14-interact-with-pdf-files" /
    "practice_files" / 
    "expense_reports"
)

for path in reports_dir.glob("*.pdf"):
    print(path.name)
    
expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()

for path in expense_reports:
    print(path.name)
    
#created new instance
pdf_merger = PdfMerger()

#looped over the paths in the sorted expense_reports
for path in expense_reports:
    pdf_merger.append(str(path))
    
with Path("expense_reports.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
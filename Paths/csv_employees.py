import csv
from pathlib import Path

'''employees = [
    ["name","department","salary"]
    ["Lee","Operations",75000.00]
    ["Jane","Engineering",85000.00]
    ["Diego","Sales",80000.00]
]'''

file_path = Path.home() / "employees.csv"
file = file_path.open(mode = "r", encoding = "utf-8", newline="")
reader = csv.DictReader(file)

reader.fieldnames

for row in reader:
    print(row)
    
    
file.close()

def process_row(row):
    row["sal"]
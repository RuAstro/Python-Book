from pathlib import Path

file_path = Path.home() / "starships.txt"
with file_path.open(mode = "w", encoding = "utf-8")as file:
    file.writelines(starships)

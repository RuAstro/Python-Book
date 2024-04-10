from pathlib import Path
path = Path.home() / "hello.txt"
with path.open(mode = "r", encoding = "utf-8") as file:
    text = file.read()
        
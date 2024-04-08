from pathlib import Path
path = Path.home() / "hello.txt"
path.touch()
file = path.open(mode = "r", encoding = "utf-8")
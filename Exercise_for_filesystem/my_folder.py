
from pathlib import Path
new_dir = Path.home() / "my_folder"
#new_dir.mkdir()

file_path = new_dir / "file1.txt"
file_path.touch()

file_path = new_dir / "file2.txt"
file_path.touch()

image1 = new_dir / "image1.jpg"
image1.touch()
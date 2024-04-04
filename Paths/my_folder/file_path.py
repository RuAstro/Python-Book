from pathlib import Path

file_path = Path.home()  #Path.home() class method creates a Path object representing the home directory.

print(file_path.exists())

pathlib.Path.home().joinpath ("my_folder").joinpath ("my_file.txt")
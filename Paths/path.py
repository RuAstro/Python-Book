from pathlib import Path

path = Path("C:/Users/edit.txt")
#get file name
print(path.name)

#get the directory name
print(path.parent)

#get file extension
print(path.suffix)

#name without extension
print(path.stem)

from pathlib import Path

#Path Object
path = Path("Users\User\Desktop\Python BOOK")

#Check if path exists
print("Exists", path.exists())

#check if its a directory
print("Is directory:", path.is_dir())

#List all items in the directory
print("Items in directory:")
for item in path.iterdir():
    print(item)
    

#Join paths to create a new path
new_path = path / "new_directory" / "new_file.txt"
print("New path:", new_path)


#get the parent directory
parent_directory = path.parent
print("Parent directory:", parent_directory)

#get stem of the path
stem = path.stem
print("Stem:", stem)

#get file extension
suffix = path.suffix
print("Suffix:", suffix)

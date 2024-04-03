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
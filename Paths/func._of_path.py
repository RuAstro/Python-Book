from pathlib import Path

#Path Object
path = Path("Users\User\Desktop\Python BOOK")

#Check if path exists
print("Exists", path.exists())

#check if its a directory
print("Is directory:", path.is_dir())
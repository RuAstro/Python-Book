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

#Checking Path Existence and Type
print(path.exists())

print(path.is_file())

print(path.is_dir())


#Reading and writing files
contents = path.read_text()
print(contents)

path.write_text("Hello, World!")


#Listing Directory Contents
for item in path.iterdir():
    print(item)
    
    
    
#Joining Paths
new_path = path / "new_directory" / "new_file.txt"
print(new_path)



#Resolving Symbolic Links
resolved_path = path.resolve()
print(resolved_path)
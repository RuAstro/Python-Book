#After importing the Path class, you create a new path to a directory
#called new_directory/ in your home folder and assign this path to the
#new_dir variable. Then you use .mkdir() to create the new directory.
 

from pathlib import Path
new_dir = Path.home() / "new_directory"
print(new_dir.exists())
#new_dir.mkdir()

print(new_dir.exists())

print(new_dir.is_dir())

print(new_dir.mkdir(exist_ok = True))

if not new_dir.exists():
    new_dir.mkdir()
    
nested_dir = new_dir / "folder_a" / "folder_b"
#nested_dir.mkdir(parents = True)


file_path = new_dir / "file1.txt"
file_path.touch("file1.txt")

file_path.exists()
file_path.is_file()


file_path = new_dir / "folder_c" / "file2.txt"
#file_path.parent.mkdir()
file_path.touch()


for path in new_dir.iterdir():
    print(path)
    

for path in new_dir.glob("*.txt"):
    print(path)
   
#Convert the returned value of .glob() to a list 
#list(new_dir.glob("*.txt"))

paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
]

for path in paths:
    path.touch()
    
    
#list(new_dir.glob("*.py"))
#list(new_dir.glob("*1*"))
#list(new_dir.glob("program?.py"))
#list(new_dir.glob("?older_?"))
#list(new_dir.glob("*1.??"))
#list(new_dir.glob("program[13].py"))
#list(new_dir.glob("**/*.txt"))
#list(new_dir.glob("**/*.py"))

#most people use this method.
list(new_dir.rglob("*.py"))
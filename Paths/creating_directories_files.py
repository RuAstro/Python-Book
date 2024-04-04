#After importing the Path class, you create a new path to a directory
#called new_directory/ in your home folder and assign this path to the
#new_dir variable. Then you use .mkdir() to create the new directory.
 

from pathlib import Path
new_dir = Path.home() / "new_directory"
print(new_dir.exists())
new_dir.mkdir()

print(new_dir.exists())

print(new_dir.is_dir())

print(new_dir.mkdir(exist_ok = True))
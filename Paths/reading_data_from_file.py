from pathlib import Path
path = Path.home() / "hello.txt"
with path.open(mode = "r", encoding = "utf-8") as file:
    text = file.read()
        
text


with path.open(mode = "r", encoding = "utf-8") as file:
    for line in file.readlines():
        print(line, end = "")
        

with path.open(mode = "w", encoding = "utf-8") as file:
    file.write("Hi there!")
    
    
with path.open(mode = "r", encoding = "utf-8") as file:
    text = file.read()
    
print(text)


with path.open(mode = "a", encoding = "utf-8") as file:
    file.write("\nHello")
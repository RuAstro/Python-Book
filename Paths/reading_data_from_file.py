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
    
with path.open(mode = "r", encoding = "utf-8") as file:
    text = file.read()
    
print(text)


lines_of_text = [
    "Hello from line1\n",
    "Hello from line2\n",
    "Hello from line3\n", 
]

with path.open(mode = "w", encoding = "utf-8") as file:
    file.writelines(lines_of_text)
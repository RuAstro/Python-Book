file_path = "C:/Users/User/hello.txt"
file = open(file_path, mode="r", encoding = "utf-8")
file
file.close()

#the With statement...
with open(file_path, mode = "r", encoding = "utf-8") as file:
#while True:
  #  try:
   #     my_input = input("Input an Integer: ")
   #     print(int(my_input))
   #     break
   # except ValueError:
   #     print("try again")
        
    
input_string = input("Enter a string: ")

try:
    index = int(input("Enter a integer: "))
    print(input_string[index])
except ValueError:
    print("Invalid number")
except IndexError:
    print("Index is out of bounds")
my_input = input("Type in a word: ")

if len(my_input) < 5:
    print("Your input is less than 5 characters long")
elif len(my_input) > 5:
    print("Your input is greather than 5 characters long")

else:
    print("Your input is 5 characters long")
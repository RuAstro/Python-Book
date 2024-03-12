my_input = input("Type in a word: ")

if len(my_input) < 5:
    print("Your input is less than 5 characters long")
elif len(my_input) > 5:
    print("Your input is greather than 5 characters long")

else:
    print("Your input is 5 characters long")
    
    
    
print("I'm thinking of a number between 1 and 10. Guess which one. ")
my_geuss = input("What number are you Geussing? ")

if my_geuss == "3":
    print("you win!")
    
else:
    print("you lose.")
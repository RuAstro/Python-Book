user_num = int(input("Enter a positive integer: "))
for divisor in range(1, user_num + 1):
    if user_num % divisor == 0:
        print(f"{divisor} is a factor of {user_num}. ")

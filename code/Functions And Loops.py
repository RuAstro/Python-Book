def multiply(x, y):
    product = x * y
    return product

    num = multiply(2, 4)
    print(num)


def greet(RJ):
    print(f"Hello, {name}!" )

def cube(num):
    """return the cube of the input number."""
    cube_num = num**3
    return cube_num

print(f"0 cubed is {cube(0)}")
print(f"2 cubed is {cube(2)}")

def convert_cel_to_far(temp_cel):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    temp_far = temp_cel *(9 / 5) + 32
    return temp_far
    
print(convert_cel_to_far(5))

def convert_far_to_cel(temp_far):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    temp_cel = temp_far - 32 *(5 / 9)
    return temp_cel

print(convert_far_to_cel(20))


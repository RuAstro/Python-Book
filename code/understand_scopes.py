#x = "Hello, World"

#def func():
 #   x = 2
 #   print(f"Inside 'func', x has the value {x}")


#func()
#print(f"Outside 'func', x has the value {x}")




total = 0

def add_to_total(n):
    global total
    total = total + n 

add_to_total(5)
print(total)

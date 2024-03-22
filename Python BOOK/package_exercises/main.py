from helpers.string import shout
from helpers.math import area

length = 5
width = 8

message = (f"The area of A {length}-by-{width} rectangle is {area(length, width)} ")  
print(shout(message))
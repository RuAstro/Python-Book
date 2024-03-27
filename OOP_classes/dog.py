class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old!"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetriever:
    def speak(self, sound = "Bark"):
        return f"Your dog says {sound}"
    
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
        return length * width
    
class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        
square = Square(4)
print(square.area)

square.width = square.width(5)
print(square.width)
    
    
    
    
    
    
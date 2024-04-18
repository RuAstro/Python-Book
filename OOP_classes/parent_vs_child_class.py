
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age= age
        
        
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    
    
    
class JackRusselTerrier(Dog):
    def speak(self, sound = "Arf"):
            return f"{self.name} says {sound}"
    
    class Dachshunds(Dog):
        def speak(self, sound = "Grrr"):
            return f"{self.name} says {sound}"
            
    class Bulldog(Dog):
        def speak(self, sound = "Woof"):
            return f"{self.name} says {sound}"
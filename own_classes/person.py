
class Person:

    def __init__(self, name, surname, age, height, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        
    def walk(self):
        print("Walking...")
        
    def run(self):
        print("Running...")
        
    def coral(self):
        print("carolling...")
        
    user = ("RJ", "VH", 19, 1.78, 90)
    
    print(f"The user details: {user}.")
    
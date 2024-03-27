
class Person:

    def __init__(self, name, surname, age, height, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        
    def BMI(self):
        bmi = self.weight // (self.height*self.height)
        print(f"BMI for {self.name} is {bmi}")
        
    def run(self):
        print("Running...")
        
    def coral(self):
        print("carolling...")
        
        
user1 = Person("RJ", "VH", 19, 1.78, 90)
user2 = Person("JC", "Jardim", 41 ,1.88, 98 )
    
print(f"The user details: {user1}.")
    
user1.BMI()
user2.BMI()
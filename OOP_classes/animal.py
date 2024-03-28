class Animal:
    
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        
    def walking(self, walk):          #instance method!
        return f"{self.name} is a {self.sex} and is walking {walk} km/h. "
    
    def eating(self, food):
        return f"{self.name} only eats {food}."
    
    def sleeping(self):
        pass
    
    def speak(self, sound):
        return f"{self.name} is a {self.sex}, and makes a {sound} sound."
        
            
    
class Pig(Animal):
    def speak(self, sound = "Gggg Gggg"):
        return super().speak(sound)
    
    def walking(self, walk = "1"):
        return super().walking(walk)
    
    def eating(self, food = "Biltong"):
        return super().eating(food)


class Monkey(Animal):
    def speak(self, sound = "Ahhh haaa"):
        return super().speak(sound)
    
    def walking(self, walk = "4"):
        return super().walking(walk)
    
    def eating(self, food = "Banana"):
        return super().eating(food)


class Donkey(Animal):
    def speak(self, sound = "Ihhh brrr"):
        return super().speak(sound)
    
    def walking(self, walk = "2"):
        return super().walking(walk)
    
    def eating(self, food = "Appels"):
        return super().eating(food)
        
        
#instance speak...walk...
babe = Pig("Babe", "male")
print(babe.speak())
print(babe.walking())

flow = Monkey("Flow", "female")
print(flow.speak())
print(flow.walking())


lady = Donkey("Lady", "female")
print(lady.speak())
print(lady.walking())


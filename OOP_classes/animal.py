class Animal:
    
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        
    def walking(self, walk):          #instance method!
        return f"{self.name} is a {self.sex} and is walking {walk} km/h. "
    
    def running(self):
        pass
    
    def eating(self):
        pass
    
    def sleeping(self):
        pass
    
    def speak(self, sound):
        return f"{self.name} is a {self.sex}, and makes a {sound} sound."
        
            
    
class Pig(Animal):
    def speak(self, sound = "Gggg Gggg"):
        return super().speak(sound)
    
    def walking(self, walk = "5"):
        return super().walking(walk)


class Monkey(Animal):
    def speak(self, sound = "Ahhh haaa"):
        return super().speak(sound)
    
    def walking(self, walk = "10"):
        return super().walking(walk)


class Donkey(Animal):
    def speak(self, sound = "Ihhh brrr"):
        return super().speak(sound)
    
    def walking(self, walk):
        return super().walking(walk)
        
        
#instance speak...
babe = Pig("Babe", "male")
print(babe.speak())
print(babe.walking())

flow = Monkey("Flow", "female")
print(flow.speak())
print(flow.walking())


lady = Donkey("Lady", "female")
print(lady.speak())
print(lady.walking())

#instance walk...
# babe = Pig("Babe", "male")
# print(babe.walking())

# flow = Monkey("Flow", "female")
# print(flow.walking())

# lady = Donkey("Lady", "female")
# print(lady.walking())
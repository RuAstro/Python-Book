class Animal:
    
    def __init__(self, name, sex):
        self.name = name
        self.sexual_type = sex
        
    def walking(self):          #instance method!
        return f"{self.name} is a {self.sexual_type} and is walking alone..."
    
    def running(self):
        pass
    
    def eating(self):
        pass
    
    def sleeping(self):
        pass
    
    def speak(self, sound):
        return f"The sound of the {self.name} makes {sound}. "
        
            
    
class Pig(Animal):
    def speak(self, sound = "Gggg Gggg"):
        return super().speak(sound)


class Monkey(Animal):
    def speak(self, sound = "Ahhh haaa"):
        return super().speak(sound)


class Donkey(Animal):
    def speak(self, sound = "Ihhh brrr"):
        return super().speak(sound)
        
        
#instance     
babe = Pig("Babe", "male")
print(babe.speak())
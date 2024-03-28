class Animal:
    
    def __init__(self, name, sexual_type):
        self.name = name
        self.sexual_type = sexual_type
        
    
class Pig(Animal):
    def speak(self, sound = "Gggg Gggg"):
        return super.speak(sound)


class Monkey(Animal):
    def speak(self, sound = "Ahhh haaa"):
        return super.speak(sound)


class Donkey(Animal):
    def speak(self, sound = "Ihhh brrr"):
        return super.speak(sound)
        
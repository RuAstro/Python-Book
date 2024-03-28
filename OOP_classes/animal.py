class Animal:
    
    def __init__(self, name, sexual_type):
        self.name = name
        self.sexual_type = sexual_type
        
    
class Pig:
    def speak(self, sound = "Gggg Gggg"):
        return super.speak(sound)


class Monkey:
    def speak(self, sound = "Ahhh haaa"):
        return super.speak(sound)



class Donkey:
    def speak(self, sound = "Ihhh brrr"):
        return super.speak(sound)
        
class Phone:
    
    def __init__(self, type, model, length, weight, color):
        self.type = type
        self.model = model
        self.length = length
        self.weight = weight
        self.color = color
        
    def phone_type(self, type):
        return f"The phone name is {type}."
    
    def phone_model(self, model):
        return f"The model of the phone is {model}."
    
    def phone_length(self, length):
        return f"The length of the phone is {length}"
    
    def phone_weight(self, weight):
        return f"The weight of the phone is {weight}"
    
    def phone_color(self, color):
        return f"The color of the phone is {color}"
        


class apple(Phone):

    def phone_type(self, type = "iPhone XR"):
        return super().phone_type(type)
    
    def phone_model(self, model = "2018"):
        return super().phone_model(model)
    
    def phone_length(self, length = "15 cm"):
        return super().phone_length(length)
    
    def phone_weight(self, weight = "0.5 kg"):
        return super().phone_weight(weight)
    
    def phone_color(self, color = "Black"):
        return super().phone_color(color)
    
    
xr = apple("XR")
print(xr.type())
print(xr.model())
print(xr.length())
print(xr.weight())
print(xr.color())
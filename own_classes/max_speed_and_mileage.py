class Car:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        
CarX = Car(200, 28)
print(CarX.max_speed, CarX.mileage)
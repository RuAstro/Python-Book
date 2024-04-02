class Car:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        
# CarX = Car(200, 28)
# print(CarX.max_speed, CarX.mileage)

class Bus(Car):
    pass

Car_Name = Bus("Volvo", 100, 15)
print("Car Name: ",Car_Name.name , "Speed: ",Car_Name.max_speed, "Mileage: ",Car_Name.mileage)
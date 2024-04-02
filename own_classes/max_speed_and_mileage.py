class Car:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        
# CarX = Car(200, 28)
# print(CarX.max_speed, CarX.mileage)

    def seating_capacity(self, capacity):
        return  f"The seating capacity of a {self.name} is {capacity} passengers."


class Bus(Car):
    def seating_capacity(self, space = 50):
        return super().seating_capacity()

Car_Name = Bus("Volvo", 100, 15)
print("Car Name: ",Car_Name.name , "Speed: ",Car_Name.max_speed, "Mileage: ",Car_Name.mileage)
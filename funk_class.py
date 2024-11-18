class Car:
    def __init__(self, brand, modell, year):
        self.brand = brand
        self.modell = modell
        self.year = year

    def is_starting(self):
        print(f"{self.modell} is starting")
    
    def is_stopped(self):
        print(f"{self.modell} is stopped")
        

class ElectricCar(Car):
    def __init__(self, brand, modell, year, battery_capacity):
        super().__init__(brand, modell, year)
        self.battery_capacity = battery_capacity



el_car = ElectricCar("Tesla", "Model X", 2024, 80)
car1 = Car("VW", "Passat", 2016)
car2 = Car("Porshe", "cayenne", 2022)

el_car.is_starting()

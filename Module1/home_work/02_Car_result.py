class Car:
    def __init__(self, gaz_level, gaz_max, fuel_consumption_100km):
        self.gaz_level = gaz_level
        self.gaz_max = gaz_max
        self.fuel_consumption_100km = fuel_consumption_100km
        self.mileage = 0

    def fill(self, add_fuel) -> None:
        if add_fuel > 0:
            if self.gaz_level + add_fuel <= self.gaz_max:
                self.gaz_level += add_fuel
                print(f"заправлено литров: {add_fuel}")
            else:
                print(f"Лишнее топливо: {add_fuel + self.gaz_level - self.gaz_max }")
                self.gaz_level = self.gaz_max

    def ride(self, km) -> None:
        cons = (km / 100) * self.fuel_consumption_100km
        if cons <= self.gaz_level:
            self.mileage += km
            self.gaz_level -= cons
        else:
            self.mileage += (self.gaz_level / self.fuel_consumption_100km) * 100
            self.gaz_level = 0

car1 = Car(gaz_level = 50, gaz_max = 100, fuel_consumption_100km = 10)

car1.fill(60)

car1.ride(300)
print(car1.gaz_level)

car1.ride(500)
print(car1.gaz_level)

car1.ride(200)
print(car1.gaz_level)

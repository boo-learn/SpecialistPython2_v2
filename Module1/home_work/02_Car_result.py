## Автомобиль

class Car:
    def __init__(self, gas, capacity, gas_per_km,odometer):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.odometer = odometer

    def fill(self, litres):
        litres_in_tank = self.gas + litres
        if litres_in_tank > self.capacity:
            self.gas = self.capacity
            extra_litres = litres_in_tank - self.capacity
            print(f"your tank is full, these {extra_litres} litres are extra")
        else:
            self.gas = litres_in_tank

    def ride(self, km):
        fuel_use = km * self.gas_per_km
        if fuel_use > self.capacity:
            remaining_mileage = self.capacity / self.gas_per_km
            self.odometer = self.odometer + remaining_mileage
            self.gas = 0
            print(f"we have driven only {remaining_mileage} and ran out of gas")
        else:
            self.gas = self.gas - fuel_use
            self.odometer = self.odometer + km





car1 = Car(9,35,0.07,121000)
print(car1.__dict__)
#заправка
car1.fill(60)
print(car1.__dict__)
#поездка
car1.ride(700)
print(car1.__dict__)

#пункт д не стал реализовывать, так как это не типовое поведение обьекта машина

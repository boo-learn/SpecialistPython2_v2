class Car:
    def __init__(self):
        self.gas = 0
        self.capacity = 100
        self.gas_per_km = 0.08
        self.mileage = 0

    def fill(self, litre):
        to_full = self.capacity - self.gas
        if litre > to_full:
            self.gas = self.capacity
            print(f"Не вместилось литров: {litre - to_full}")
        else:
            self.gas = litre

    def ride(self, km):
        gas_consumption = self.gas_per_km * km
        if self.gas - gas_consumption < 0:
            self.mileage += self.gas / self.gas_per_km
            print(f"Проехали {self.gas / self.gas_per_km} из {km} км, топливо: 0, пробег: {self.mileage}")
            self.gas = 0
        else:
            self.gas -= gas_consumption
            self.mileage += km
            print(f"Проехали {km} из {km} км, топливо: {self.gas}, пробег: {self.mileage}")


car = Car()
car.fill(160)
car.ride(1000)
car.fill(80)
car.ride(1000)

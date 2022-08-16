class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage = 0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0
    
    def fill(self, gas_added):
        if self.gas + gas_added <= self.capacity:
            self.gas += gas_added
        else:
            excess_gas = self.gas + gas_added - self.capacity
            print(f"Лишние литры - {excess_gas} ")
            self.gas = self.capacity
    
    def ride(self, path_length):
        gas_needs = path_length * self.gas_per_km
        if gas_needs <= self.gas:
            self.gas -= gas_needs
            self.mileage += path_length
            print(f"Проехали {path_length} километров")
        else:
            print(f"Проехали {self.gas / self.gas_per_km} километров\n")
            self.mileage += self.gas / self.gas_per_km
            self.gas = 0
    
    def show(self):
        return f"Остаток бензина {self.gas}л     Вместимость бака {self.capacity}л     Расход {self.gas_per_km}л/км     Пробег {self.mileage}км\n"
            

print()
car1 = Car(60, 100, 0.5)

car1.fill(55)  # залили 5 литров
print(car1.show())

car1.ride(100)
print(car1.show())

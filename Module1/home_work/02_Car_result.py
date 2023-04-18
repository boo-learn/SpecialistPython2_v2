class Car:
    def __init__(self, capacity, gas_per_km, gas=0):
        self.gas = gas  # бензина в баке
        self.capacity = capacity  # Объем бака
        self.gas_per_km = gas_per_km   # Расход на 1 км
        self.mileage = 0  # Пробег

    def fill(self, quantity: (int, float)) -> None:
        if quantity < self.capacity:
            self.gas = quantity
        else:
            self.gas = self.capacity
            remain = quantity - self.capacity
            print(f"В баке {self.capacity}, не влезло {remain}")

    def ride(self, distance: (int, float)) -> None:
        spend_gas = distance*self.gas_per_km
        if spend_gas > self.gas:
            self.mileage += self.gas/self.gas_per_km
            way_to_go = distance - self.gas/self.gas_per_km
            self.gas = 0
            print(f"Топливо кончилось, осталось до пункта назначения {way_to_go}")
        else:
            self.mileage += distance
            self.gas -= spend_gas

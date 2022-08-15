class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = mileage

    def fill(self, put):
        if self.gas + put > self.capacity:
            self.gas = self.capacity
            print("бак заполнился полностью, остались лишние литры: ")
        else:
            self.gas += put

    def show(self):
        return f"количество бензина: {self.gas} вместимость:{self.capacity} расход:{self.gas_per_km}"

    def ride(self, put):
        if self.gas_per_km * put > self.gas:
            self.mileage += self.gas / self.gas_per_km

            print(f"Бензин закончится до конца пути, максимум можно проехать {self.gas / self.gas_per_km } км, пробег {self.mileage}")
        else:
            self.mileage += put
            print(f"Можно проехать все {put } км, пробег {self.mileage}")


car1 = Car(10, 50, 2, 0)
print(car1.show())
car1.fill(49)
car1.ride(28)

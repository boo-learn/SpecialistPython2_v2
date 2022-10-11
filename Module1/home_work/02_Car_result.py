class Car:
    def __init__(self, gas: float, capacity: float, gas_per_km: float, run: float):
        self.gas = gas # сколько бензина в баке
        self.capacity = capacity # вместимость бака
        self.gas_per_km = gas_per_km # расход топлива на км\
        self.run = run # пробег

    def fill(self, new_gas) -> float: # метод "залить столько-то литров в бак"
        if (self.gas + new_gas) > self.capacity:
            print(f"Лишние литры: {(self.gas + new_gas) - self.capacity}")
            self.gas = self.capacity
        else:
            self.gas = self.gas + new_gas

    def ride(self, km) -> float: # проехать сколько-то км"
        if km <= self.gas / self.gas_per_km:
            self.gas = self.gas - km * self.gas_per_km
            print(f"Проехали {km} километров")
            self.run = self.run + km
        else:
            self.gas = 0
            print(f"Проехали {self.gas / self.gas_per_km} километров")
            self.run = self.run + self.gas / self.gas_per_km


    # def show(self) -> str:
    #     return f"{self.gas} вес:{self.capacity} цена:{self.gas_per_km}"

car1 = Car(0, 100, 2, 10)
print(car1.gas)
car1.fill(108)
print(car1.gas)
car1.ride(25)
print(car1.run)
print(car1.gas)

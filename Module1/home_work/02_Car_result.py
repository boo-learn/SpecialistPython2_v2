# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capaciti, gas_per_km, km=0):
        self.gas = gas
        self.capaciti = capaciti
        self.gas_per_km = gas_per_km
        self.km = km


    def fill(self, liter):
        capaciti = self.capaciti

        if capaciti >= self.gas + liter:
            self.gas = self.gas + liter
            return self.gas
        else:
            self.gas = self.capaciti
            print(f'лишних литров {self.gas + liter - self.capaciti} ')
            return self.gas

    def ride(self, km):
        if self.gas_per_km * km <= self.gas:
            self.gas = self.gas - self.gas_per_km * km
            self.km += km
            print(f'Проехали {km} киллометров')
            return self.gas
        else:
            print(f'Недостаточно топлива')


car1 = Car(5, 30, 0.1)

print(car1.ride(40))
print(car1.fill(5))
print(car1.ride(40))
print(car1.km)

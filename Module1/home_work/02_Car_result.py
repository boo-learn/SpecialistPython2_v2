# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km, run):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.run = run

    def fill(self, litres):
        if self.capacity - self.gas >= litres:
            self.gas += litres
        else:
            print(f'Не вместилось {litres - (self.capacity - self.gas)} литров')
            self.gas = self.capacity

    def ride(self, km):
        if self.gas < (km * self.gas_per_km):
            print(f'Проехали {self.gas / self.gas_per_km} километров')
            self.run += self.gas / self.gas_per_km
            self.gas = 0
        else:
            print(f'Проехали {km} километров' )
            self.run += km
            self.gas -= km * self.gas_per_km
            

# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = mileage

    def fill(self, litres):
        if self.gas + litres > self.capacity:
            print(f'Не влезло {self.gas + litres - self.capacity} литров')
            self.gas = self.capacity
        else:
            self.gas += litres

    def ride(self, distance):
        if self.gas / self.gas_per_km < distance:
            distance = self.gas / self.gas_per_km
        print(f' Едем {distance} километров')
        self.gas -= self.gas_per_km * distance
        self.mileage += distance


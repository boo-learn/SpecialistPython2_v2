# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:

    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0

    def fill(self, liters):
        if self.gas + liters > self.capacity:
            print(f"Бак заполнен полностью. Обнаружено {self.gas + liters - self.capacity} лишних литров")
            self.gas = self.capacity
            return
        self.gas = self.gas + liters

    def ride(self, km):
        available_km = int(self.gas / self.gas_per_km)
        if available_km >= km:
            self.gas = self.gas - self.gas_per_km * km
            print(f'Проехали требуемые {km} км')
            self.mileage += km
        else:
            self.gas = self.gas - self.gas_per_km * available_km
            print(f'Проехали {available_km} км из {km} км требуемых')
            self.mileage += available_km


car1 = Car(15, 65, 5)

car1.ride(4)

car1.fill(65)

car1.ride(13)

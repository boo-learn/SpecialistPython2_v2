# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md
# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gpk, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gpk
        self.mileage = mileage

    def fill(self, amount):
        if self.gas + amount <= self.capacity:
            self.gas = self.gas + amount
            print("Машина заправлена. Объем бака:", self.gas, "л")
        else:
            self.gas = self.capacity
            print('Превышена вместительность. Залит полный бак. Объем бака:', self.gas, 'л')

    def ride(self, km):
        if km * self.gas_per_km <= self.gas:
            self.mileage = self.mileage + km
            self.gas = self.gas - km * self.gas_per_km
            print("Машина проехала", km, "километров. Запас топлива", self.gas, "литров Пробег:", self.mileage)


        else:
            self.mileage = self.mileage + int(self.gas / self.gas_per_km)
            print("Машина проехала", int(self.gas / self.gas_per_km), "км и заглохла. Пробег:",
                  self.mileage)


car1 = Car(50, 100, 2, 15000)
car1.ride(10)
car1.fill(40)
car1.ride(25)
car1.fill(100)
car1.ride(100)

# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas: int, capacity: int, gas_per_km: int):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km

    def fill(self, benz: int):
        self.benz = benz
    def __str__(self):
        return f'Gas: {self.gas}, capacity: {self.capacity}, gas_per_km: {self.gas_per_km}'

    def ride(self, distance: int):
        self.dist = distance
        result = self.gas - (distance * self.gas_per_km)
        while self.gas != 0:
            self.gas = result
            print("Едем дальше")
        else:
            print("stop")

car1 = Car(15, 20, 1)
print(car1)
car1.fill(10)
print(car1)
car1.ride(10)

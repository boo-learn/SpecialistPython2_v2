# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.ride = 0

    def fill(self, gas):
        if self.gas + gas < self.capacity:
            self.gas = self.gas + gas
        else:
            print(self.gas + gas - self.capacity, "Лишних литров")
            self.gas = self.capacity

    def drive(self, dist):
        if self.gas < self.gas_per_km * dist:
            self.ride = self.ride + self.gas / self.gas_per_km
            print("Проехали",self.gas / self.gas_per_km,"километров" )
            self.gas = 0
        else:
            self.ride = self.ride + dist
            print("Проехали",dist,"километров" )
            self.gas = self.gas - dist * self.gas_per_km

car1 = Car(45, 50, 5)

car1.fill(7)

print(car1.gas)

car1.drive(5)

print("Осталось топлива ", car1.gas)
print("Пробег ",car1.ride)

car1.drive(15)

print("Осталось топлива ", car1.gas)
print("Пробег ",car1.ride)

# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, capacity, gas_per_km):
        self.gas = 0
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.run = 0

    def fill(self, litres):
        if self.capacity - self.gas < litres:
            print(f"{litres - self.capacity + self.gas} лишних литров")
            self.gas = self.capacity
        else:
            self.gas += litres

    def ride(self, km):
        if self.gas / self.gas_per_km >= km:
            print(f'проехали {km} километров')
            self.gas -= km * self.gas_per_km
            self.run += km
        else:
            print(f"проехали {self.gas / self.gas_per_km} километров")
            self.run += self.gas / self.gas_per_km
            self.gas = 0

    def show(self):
        return f'топливо {self.gas} л., расход {self.gas_per_km} л./км., пробег {self.run} км., объём {self.capacity} л.'


car1 = Car(80, 0.25)
car1.fill(100)
car1.ride(1000)
print(f"car1: {car1.show()}")

car2 = Car(80, 0.25)
car2.fill(20)
car2.ride(5)
print(f"car2: {car2.show()}")

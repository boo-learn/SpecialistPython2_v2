# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md


class Car:
    def __init__(self, a, b, c):
        self.gas = a
        self.capacity = b
        self.gas_per_km = c
        self.distance = 0

    def fill(self, a):
        if self.gas + a > self.capacity:
            self.gas = self.capacity
            print(f"{a-self.capacity} лишних литра")
            return self.gas
        elif self.gas + a <= self.capacity:
            self.gas += a
        return self.gas

    def ride(self, km):
        if km * self.gas_per_km > self.gas:
            self.distance += self.gas / self.gas_per_km
            return print(
                f" машина проехала {self.gas/self.gas_per_km} км, топливо закончилось"
            )
        else:
            self.distance += km
            return print(f" машина проехала {km} км")


car1 = Car(40, 60, 0.5)

car1.fill(20)

car1.ride(100)

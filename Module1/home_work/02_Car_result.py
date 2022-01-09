# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md
import random


class Car:
    def __init__(self):
        self.capacity = random.randint(1, 100)
        self.gas = random.randint(0, self.capacity)
        self.gas_per_km = random.uniform(1, 10)
        self.use = 0

    def fill(self, gas):
        self.gas += gas
        if self.gas > self.capacity:
            print(
                f"Бак переполнен\nЛишнее топливо: {self.gas-self.capacity}л\nТоплива в баке: {self.capacity}л"
            )
            self.gas = self.capacity
        elif self.gas == self.capacity:
            print(f"Полный бак\nТоплива в баке: {self.gas}л")
        elif self.gas < self.capacity:
            print(f"Бак не полный\nТоплива в баке: {self.gas}л")

    def ride(self, km):
        f_used = km * self.gas_per_km
        if f_used > self.gas:
            print(
                f"Недостаточно топлива, чтобы проехать {km} км\nАвтомобиль проехал только {self.gas/self.gas_per_km}"
            )
            self.use += self.gas / self.gas_per_km
            self.gas = 0
        else:
            self.gas -= f_used
            self.use += km
            print(f"Автомобиль проехал {km}км\n В баке осталось топлива: {self.gas}л")

    def pr_gas(self):
        print(f"Топлива в баке: {self.gas}л")

    def pr_capacity(self):
        print(f"Объём бака {self.capacity}л")

    def pr_gas_per_km(self):
        print(f"Расход топлива: {self.gas_per_km}л/км")

    def pr_use(self):
        print(f"Пробег автомобиля: {self.use}км")

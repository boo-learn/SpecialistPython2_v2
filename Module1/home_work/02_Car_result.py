# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km):
        """
        сколько бензина в баке gas
        вместимость бака capacity
        расход топлива на км gas_per_km
        """
        self.count_gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km

    def fill(self, x):
        # залить столько-то литров в бак
        if self.count_gas + x <= self.capacity:
            self.count_gas = self.count_gas + x
        else:
            self.count_gas = self.capacity
            print('остались лишние литры')

    def ride(self, x):
        # проехать сколько-то км
        max_km = self.count_gas / self.gas_per_km
        if x > max_km:
            self.count_gas = 0
            print(f'Проехали {max_km} км')
        else:
            self.count_gas = self.count_gas - x * self.gas_per_km
            print(f'Проехали {x} км')


car_1 = Car(20, 100, 5)
print(car_1.count_gas)
car_1.fill(100)
print(car_1.count_gas)
car_1.ride(5)
car_1.ride(10)
print(car_1.count_gas)
car_1.fill(20)
car_1.ride(8)
print(car_1.count_gas)


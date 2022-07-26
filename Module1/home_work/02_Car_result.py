# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    pass
    def __init__(self, gas, capacity, gas_per_km, car_mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.car_mileage = car_mileage

    def fill(self, petrol):
        if self.gas + petrol > self.capacity:
            print("Лишних литров: ", self.gas + petrol - capacity)
            self.gas = self.capacity
        else:
            self.gas += petrol
    def ride(self, km):
        if km * self.gas_per_km > self.gas:
            self.car_mileage = self.car_mileage + (self.gas / self.gas_per_km)
            return print(f" Машина проехала {self.gas/self.gas_per_km}, км, бензин закончился")
        self.mileage = self.mileage + km
        return print(f" машина проехала {km} км")
car1 = Car(30, 70, 5, 500)

car1.ride(50)

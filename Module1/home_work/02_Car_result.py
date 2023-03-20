# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:

    def __init__(self, gas: int, capacity: int, gas_per_km: int):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0

    def fill(self, gas: int):
        gas_refill = self.gas + gas
        if self.capacity >= gas_refill:
            self.gas = gas_refill
        else:
            print(f"В бак больше не влезет {gas} литров")
    def ride(self, dist: int):
        cons_gas_1_km = self.gas_per_km / 100
        reserve_gas = self.gas / cons_gas_1_km
        residue_gas = reserve_gas - dist
        spent_gas = cons_gas_1_km * dist
        if residue_gas >= 0:
            self.gas -= spent_gas
            self.mileage += dist
            print(f"проехали {dist} километров в результате потратили {spent_gas}"
                  f" литров бензина можем проехать еще {residue_gas } км")
        else:
            print(f"Для поездки в {dist} км топлива {self.gas} литров в баке не хватит")

car1 = Car(20, 50, 10)
car1.fill(30)
car1.ride(20)
car1.ride(30)
car1.ride(5)

print(f" Топливо : {car1.gas} Объем бака: {car1.capacity} Расход топлива: {car1.gas_per_km}")
print(f"Пробег {car1.mileage}")

# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capaciti, gas_per_km,km=0):
        self.gas = gas
        self.capaciti = capaciti
        self.gas_per_km = gas_per_km
        self.km=km

    def fill(self, litre):
        to_full = self.capaciti - self.gas
        if litre > to_full:
            self.gas = self.capaciti
            print(f"Не вместилось литров: {litre - to_full}")
        else:
            self.gas = litre
            print(f"В машине {self.gas} литров")


    def ride(self, distance):
        if distance > (self.gas / self.gas_per_km):
            print('Проехали', int(self.gas / self.gas_per_km), 'км, кончился бензин')
            self.km += int(self.gas / self.gas_per_km)
            self.gas = 0
  
        else:
            print('Проехали', distance, 'км')
            self.km += distance
            return self.km

car1 = Car(15, 50, 0.8)
car1.fill(20)
car1.ride(200)
car1.fill(20)
car1.ride(200)
print('Общий пробег автомобиля ', car1.km, 'км.')



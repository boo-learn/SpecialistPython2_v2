# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km, car_mileage=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.car_mileage = car_mileage #пробег
        
    def fill(self, fuel_volume):
        """
        залить столько-то литров в бак
        """
        if type(fuel_volume)==int and fuel_volume>0:
            if self.gas + fuel_volume <= self.capacity:
                self.gas += fuel_volume
                print(f'Залили {fuel_volume} л')
            else:
                print(f'Пытаемся залить больше, чем может уместиться в бак, на {self.gas + fuel_volume - self.capacity}')
        else:
            print('Данные некорректны')
            
    def ride(self, distance):
        """
        проехать сколько-то км
        """
        if distance >= 0:
            if self.gas_per_km*distance > self.gas:
                print('Не хватает топлива для преодоления такого расстояния')
            else:
                #расходуем топливо в баке
                self.gas -= self.gas_per_km*distance
                print(f'проехали {distance} километров')
                self.car_mileage += distance
                
car1 = Car(20, 1000, 10)
#car1.fill(5)
car1.fill(1005)
print(car1.gas)
car1.ride(5)
car1.fill(40)
car1.ride(5)
print(car1.car_mileage)

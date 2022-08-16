# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self,name="",gas=0,capacity=50,gas_per_km=.06,mileage=0):
       # heads-орел/tails-решка
       self.__name=name
       self.__capacity=capacity
       self.gas = gas
       if self.gas>self.__capacity:
            self.gas=self.__capacity
       self.gas_per_km=gas_per_km
       self.mileage=mileage
    def __repr__(self):
        return f'Авто {self.__name}, бак: {self.gas}, пробег: {self.mileage}'
    def fill(self,litr):  # залили 5 литров
        if (self.gas+litr)>self.__capacity:
            over=(self.gas+litr)-self.__capacity
            print(f"Вы желает залить больше возможного на {over} литров")
            self.gas=self.__capacity
        else:
            self.gas=self.gas+litr
            print(f"Теперь в баке {self.gas} литров")
    def ride(self,km):
        need_petrol=km*self.gas_per_km
        if self.gas>=need_petrol:
            self.gas=self.gas-need_petrol
            self.mileage=self.mileage+km
        else:
            real_ride=self.gas*self.gas_per_km
            self.mileage=self.mileage+real_ride
            self.gas=0
            print(f"Бензин закончился, не доехали {km-real_ride}")
car1 = Car("Vitara",gas=15)
car1.fill(50) 
print(car1)

car1.ride(50) #проехать 50 
print(car1)

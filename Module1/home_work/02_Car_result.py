# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, g, c, gpk, od):
        self.gas = g
        self.capacity = c
        self.gas_per_km = gpk
        self.odometer = od
    def fill(self, fill_in):
        if fill_in<=0:
            print('Не верное значение')
        elif fill_in+self.gas>self.capacity:
            print(f"не вместилось: {fill_in+self.gas-self.capacity} л")
            self.gas=self.capacity
        elif fill_in+self.gas<=self.capacity:
            self.gas=fill_in+self.gas
        return self.gas
    def ride(self, ride):
        if ride>self.gas/self.gas_per_km:
            print(f"Недостаточно топлива проехали {self.gas*self.gas_per_km-ride} км")
            self.odometer+=self.gas*self.gas_per_km-ride
            self.gas=0
        elif ride<=self.gas/self.gas_per_km:
            print(f"Проехали {ride} км")
            self.odometer+=ride
            self.gas-=self.gas_per_km*ride

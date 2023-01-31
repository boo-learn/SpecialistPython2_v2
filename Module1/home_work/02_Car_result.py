# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas: float, capacity: float, gas_per_km: float):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
    def fill(self,fuel: float):
        if fuel > (self.capacity - self.gas):
            self.gas = self.capacity
            print('Заправились. В бак планируется залить на ' + str((self.capacity - self.gas - fuel)*(-1)) + ' л больше возможного.')
        else:
            self.gas = self.gas + fuel
        print('Заправились. В баке ' + str(self.gas) + ' л бензина.')

    run = 0
    def ride(self, km : float):

        if km > (self.gas * self.gas_per_km):
            self.run += self.gas * self.gas_per_km
            print('Проехали ' + str(self.gas * self.gas_per_km) +'км. Бензин закончился.')
        else:
            print('Проехали ' + str(km) + 'км.')
            self.run += km
        print('Пробег машины составляет ' + str(self.run) + ' км.')

car1 = Car(10,50,5)
car1.fill(25)
car1.fill(10)
car1.ride(170)
car1.ride(20)

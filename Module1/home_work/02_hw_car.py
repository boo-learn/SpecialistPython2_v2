import sys


class Car:
    def __init__(self, gas, capacity, gas_per_km, odometer):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km * (1 + 0.05 / 1000) ** odometer
        self.odometer = odometer

    def __str__(self):
        return f'Машина с {self.gas:.2f}л бензина в баке объемом {self.capacity:.2f}л' \
               f', расходом топлива {self.gas_per_km:.3f}л/км и пробегом {self.odometer:.0f}км.'

    def fill(self, gas_to_fill):
        self.gas += gas_to_fill
        if self.gas > self.capacity:
            print(f'Вы купили бензина больше чем можно долить в бак. '
                  f'Пройдите к кассу для возврата денег за {self.gas - self.capacity:.2f}л бензина.')
            self.gas = self.capacity
        print(f'Теперь в баке вашей машины залито {self.gas:.2f}л бензина.')

    def ride(self, distance):
        if self.gas_per_km * (1 + 0.05 / 1000) ** distance * distance > self.gas:
            d = 1
            gpk = self.gas_per_km
            dist1 = 0
            while d > 0.01:  # метод последовательных итераций
                dist = self.gas / gpk
                gpk = self.gas_per_km * (1 + 0.05 / 1000) ** dist
                dist1 = self.gas / gpk
                d = abs(dist / dist1 - 1)
            self.odometer += int(dist1)
            self.gas = 0
            print(f'Не хватило бензина. До того, как заглох двигатель вам удалось проехать {dist1:.2f} км.')
        else:
            self.gas_per_km *= (1 + 0.05 / 1000) ** distance
            self.gas -= self.gas_per_km * (1 + 0.05 / 1000) ** distance * distance
            self.odometer += distance


while True:
    try:
        cap = int(input('Введите объем бака автомобиля, л: '))
        gp_km = float(input('Введите расход топлива, л/км: '))
        odm = int(input('Введите пробег автомобиля, км: '))
        gs = int(input('Введите кол-во бензина в баке, л: '))
        if gs > cap:
            print(f'В бак залито {cap}л бензина, остальное пролилось мимо.')
            gs = cap
        car1 = Car(gs, cap, gp_km, odm)
        print('Автомобиль готов!')
        print(car1)
        while True:
            act = input('Введите:\n f - для заправки\n r - для совершения поездки\n q - для завершения\n')
            if act == 'f':
                gtf = int(input('Введите количество бензина, л: '))
                car1.fill(gtf)
            elif act == 'r':
                dis = int(input('Введите дальность поездки, км: '))
                car1.ride(dis)
            elif act == 'q':
                sys.exit()
            else:
                print('Введены некорректные данные.')
                continue
            print(car1)
            if car1.gas == 0:
                print('Поездка завершена.')
                break
    except ValueError:
        print('Введены некорректные данные. Повторить ввод, y/n? ')
        act = input()
        if act == 'n':
            break

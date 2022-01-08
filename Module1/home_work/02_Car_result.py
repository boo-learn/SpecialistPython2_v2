# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km, run):
        self.gas = gas    #"сколько бензина в баке" (gas)
        self.capacity = capacity #"вместимость бака" - сколько максимум вмещается бензина (capacity)
        self.gas_per_km = gas_per_km #"расход топлива на км" (gas_per_km)
        self.run = run # пробег

    def fill(self, gas_add):
        self.gas_add = gas_add
        fill_gas = gas_add + self.gas
        if fill_gas > self.capacity:
            surplus = f'Залит полный бак, лишних {fill_gas - self.capacity}л бензина'
            self.gas = self.capacity
        else:
            # self.gas = fill_gas
            self.gas += gas_add
            surplus = f'Залито {gas_add} литров бензина, еще можно залить {self.capacity - self.gas} литров'
        return surplus

    def ride(self, ride_km):
        self.ride_km = ride_km
        drive = self.gas / self.gas_per_km
        if ride_km > drive:
            road = f'Проехали {drive} км, нужно заправиться, для продолжения поездки'
            self.run += drive
        else:
            road = f'Проехали {ride_km} км, осталось {self.gas - ride_km * self.gas_per_km}л бензина'
            self.run += ride_km
        return road


car1 = Car(10, 42, 2, 50)
print(f'В Машине {car1.gas}л бензина, вместимость бака - {car1.capacity}л, расход топлива {car1.gas_per_km}л на километров)\nТекущий пробег машины {car1.run}км')

# litr = int(input('Введите, сколько залить бензина в литрах: ' ))
flooded = car1.fill(40)
print(flooded)
print(f'В баке {car1.gas}л бензина')

#distace = int(input('Введите, сколько хотите проехать в км: '))
drive_go = car1.ride(100)
print(drive_go)
print(f'Пробег после поездки {car1.run} км')





# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self,gas,capacity,gas_per_km,mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = mileage

    def fill(self,fuel:float):
        if fuel >(self.capacity - self.gas):
            self.gas = self.capacity
            print('до полного бака',fuel - (self.capacity - self.gasfuel - (self.capacity - self.gas)))
        else:
            self.gas += fuel
            print('заправились на ',fuel)

    def ride (self,distance:float):
            if distance > (self.gas / self.gas_per_km):
                print("проехали",(self.gas / self.gas_per_km))
                self.mileage += self.gas / self.gas_per_km
                self.gas = 0
            else:
                print('проехали',distance)
                self.mileage += distance
            self.gas_per_km += self.gas_per_km*(0.05 *(distance / 1000))


car1 = Car(10, 50, 0.1, 30000) # автомобиль №1
car1.fill(30) # пример заправки на 30л
car1.ride(50) # пример поездки на 50км
print('Остаток бензина в автомобиле  после поездки:',car1.gas , 'л.')
print('Общий пробег автомобиля  после поездки:', car1.mileage, 'км.')
print('Текущий расход топлива автомобиля :', round(car1.gas_per_km, 4), 'л. на один км.')


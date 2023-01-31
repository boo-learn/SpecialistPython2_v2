# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas: int, capacity: int, gas_per_km: int, mileage: int):

        self.gas = gas #50 литров в баке
        self.capacity = capacity #Вместимость 50
        self.gas_per_km = gas_per_km #Расход 8л на 100км
        self.mileage = mileage #Пробег 500

    def fill(self, pour):
        result_pour = self.gas + pour

        if result_pour > self.capacity:
            print(f'Вы залили {result_pour - self.capacity} лишних литров!')

            self.gas = self.capacity

    def ride(self, kilometers):

        i = 0
        for i in range(kilometers + 1):
            if i % 100 == 0:
                self.gas -= self.gas_per_km
                if self.gas <= 0:
                    break

        self.mileage += i

        print(f'проехали {i} километров')




my_car = Car(30, 50, 8, 500)

s1 = my_car.fill(20)
s2 = my_car.ride(50)






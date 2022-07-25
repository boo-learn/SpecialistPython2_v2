# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage):
        Car.gas = gas
        Car.capacity = capacity
        Car.gas_per_km = gas_per_km
        Car.mileage = mileage

    def fill(self, new_gas):
        if new_gas > self.capacity - self.gas:
            print("Full of gas with excess of ", new_gas - self.capacity - self.gas)
            self.gas = self.capacity
        else:
            self.gas = self.gas + new_gas
        return

    def ride(self, distance):
        if distance > self.gas / self.gas_per_km:
            print("Distance made is ", self.gas / self.gas_per_km)
            new_miles = self.gas / self.gas_per_km
        else:
            print("Distance made is ", distance)
            new_miles = distance
        self.mileage += new_miles
        return


SuperCar = Car(10, 100, 10, 1000)

print(
    f"New SuperCar characteristics: \n gas supply {SuperCar.gas} \n gas capacity {SuperCar.capacity}\n gas spending {SuperCar.gas_per_km} \n mileage {SuperCar.mileage}")

NewFill = int(input("Enter volume of new gas fill "))
SuperCar.fill(NewFill)

print("New Gas Supply ", SuperCar.gas)

NewDist = int(input("Enter new distance "))
SuperCar.ride(NewDist)

print("New mileage = ", SuperCar.mileage)

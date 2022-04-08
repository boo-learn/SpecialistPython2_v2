# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas_amount, gas_capacity, gas_per_km, car_ride) -> None:
        self.gas_amount = gas_amount
        self.gas_capacity = gas_capacity
        self.gas_per_km = gas_per_km/100
        self.car_ride = car_ride
    
    def fill(self, gas):
        if gas <= (self.gas_capacity - self.gas_amount):
            self.gas_amount += gas
        else:
            excess_fuel = (self.gas_amount + gas) - self.gas_capacity

            self.gas_amount += (self.gas_capacity - self.gas_amount)
            print(f"Осталось {excess_fuel} литров.")

    def ride(self, distance):
        fuel_consumption = distance * self.gas_per_km
        if fuel_consumption <= self.gas_amount:
            self.gas_amount -= fuel_consumption
            self.car_ride += distance
            print(f"Вы проехали {distance} километров.")
        else:
            total_ride = self.gas_amount * self.gas_per_km * 100
            self.car_ride += total_ride
            self.gas_amount = 0
            print(f"Вы проехали {total_ride} километров, бензин закончился...")

# car1 = Car(25, 45, 11, 500)
# car1.ride(100)
# print(car1.gas_amount)
# car1.fill(31)
# print(car1.gas_amount)
# print(car1.car_ride)
# car1.ride(600)
# print(car1.car_ride)

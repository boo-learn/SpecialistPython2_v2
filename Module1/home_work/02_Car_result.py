class Car:
    def __init__(self, name, gas, capacity, gas_per_km, odometer):
        self.name = name
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.__mileage = odometer  # чтобы не скручивали

    def get_mileage(self):
        return self.__mileage

    def fill(self, x):
        gas_todo = self.gas + x
        if gas_todo > self.capacity:
            print(f'ERROR!! В {self.name} залили больше на {gas_todo - self.capacity} литров')
            self.gas = self.capacity
        else:
            self.gas += x

    def ride(self, y):
        will_ride = self.gas / self.gas_per_km
        if y > will_ride:
            print(f"ERROR!! на {self.name} не доедем {y - will_ride} км")
            self.gas = self.gas - (will_ride * self.gas_per_km)
            self.__mileage += will_ride
        else:
            self.gas = self.gas - (y * self.gas_per_km)
            self.__mileage += y

    def get_car_info(self):
        return f'машина {self.name} - в баке {self.gas} литров, вместимость - {self.capacity}, расход {self.gas_per_km * 100} л/100км, пробег {self.__mileage} км'


car1 = Car('bmw', 50, 60, 0.1, 4000)
car2 = Car('toyoya', 20, 25, 0.06, 0)
car3 = Car('audi', 0, 40, 0.08, 0)
print('Cначала')
print(car1.get_car_info())
print(car2.get_car_info())
print(car3.get_car_info())

car1.fill(10)
car2.fill(10)
car3.fill(39)
print('заправились')
print(car1.get_car_info())
print(car2.get_car_info())
print(car3.get_car_info())

car1.ride(1000)
car2.ride(100)
car3.ride(200)
print('покатались')
print(car1.get_car_info())
print(car2.get_car_info())
print(car3.get_car_info())

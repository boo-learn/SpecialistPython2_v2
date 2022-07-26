class Car:
    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.__mileage = 0

    def get_mileage(self):
        return self.__mileage

    def fill(self, amount):

        if self.gas + amount > self.capacity:
            print("Лишних литров: ", self.gas + amount - self.capacity)
            self.gas = self.capacity
        else:
            self.gas += amount

    def ride(self, km):

        if self.gas / self.gas_per_km * 100 >= km:
            l_ride = km
        else:
            l_ride = self.gas / self.gas_per_km * 100

        self.gas = self.gas - l_ride * self.gas_per_km / 100

        self.__mileage += l_ride

        print(f'Проехали {l_ride:.2f} километров. Остаток топлива {self.gas:.2f} л.')


car = Car(10, 60, 10)
car.fill(10)
car.fill(100)

car.ride(30)
car.ride(600)

print(f"Пробег  ", car.get_mileage())

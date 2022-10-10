class Car:
    def __init__(self, gas, capacity, gas_per_km) -> None:
        self.__gas = gas
        self.__capacity = capacity
        self.__gas_per_km = gas_per_km
        self.__lifespan = 0

    def fill(self, litre):
        if self.__gas + litre > self.__capacity:
            spilled = litre + self.__gas - self.__capacity
            self.__gas = self.__capacity
            print(f'Лишние {spilled} литров пролиты')
        else:
                self.__gas += litre

    def ride(self, km):
        if self.__gas_per_km * km < self.__gas:
            self.__gas -= self.__gas_per_km * km
            self.__lifespan += km
            print(f'Проехали {km} километров')
        else:
            rode = int(self.__gas/self.__gas_per_km)
            self.__gas = 0
            self.__lifespan += rode
            print(f'Проехали {rode} километров')
  
car1 = Car(0, 100, 2)
car1.fill(50)
car1.ride(5)
car1.ride(50)
car1.fill(111)
car1.ride(25)
print("Приехали!")

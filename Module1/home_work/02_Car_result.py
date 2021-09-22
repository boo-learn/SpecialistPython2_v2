class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km + mileage*0.00005
        self.mileage = mileage

    def fill(self, l):
        if self.gas + l >= self.capacity:
            return f"Бак полностью заполнен ({self.capacity} литров), излишек: {abs(self.capacity - (self.gas + l))} литров"
        else:
            return f"Залито {l} литров, в баке {self.gas + l} литров"

    def ride(self, km):
        if self.gas_per_km * km > self.gas:
            self.mileage = self.mileage + (self.gas / self.gas_per_km)
            return f"Бензин закончился, автомобиль проехал {self.gas / self.gas_per_km} километров"
        return f"Автомобиль проехал {km} километров"


car1 = Car(15, 65, 0.06, 0)
car2 = Car(0, 40, 0.1, 900)
car3 = Car(40, 50, 0.15, 1200)

print(car1.fill(5))
print(car1.ride(100))
print(car2.fill(45))
print(car2.ride(50))
print(car3.fill(0))
print(car3.ride(10))

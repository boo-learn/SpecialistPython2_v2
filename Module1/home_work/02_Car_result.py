class Car:
    def __init__(self, gas, capacity, gas_per_km, probeg):
        self.gas        = gas
        self.capacity   = capacity
        self.gas_per_km = gas_per_km
        self.probeg = probeg
    def fill(self, volume):
        if volume >= (self.capacity - self.gas):
            print("Лишнее : ", (volume - (self.capacity - self.gas)))
            self.gas = self.capacity
        else:
            self.gas = self.gas + volume
    def ride(self, km):
        max_km = self.gas/self.gas_per_km
        if max_km >= km:
            print("Машина проехала : ", km, "km")
            self.probeg += km
            print("Пробег : ", self.probeg, "km")
        else:
            print("Не хватило. Проехала : ", max_km)
            self.probeg += max_km
            print("Пробег : ", self.probeg, "km")


car1 = Car(30,100, 1, 120000)
print("Было : ", car1.gas)
car1.fill(500)
print("Стало : ", car1.gas)
car1.ride(30)

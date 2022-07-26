class Car:
    def __init__(self, name, gas, capacity, gas_per_km, distride):
        self.name=name
        self.gas=gas
        self.capacity=capacity
        self.gas_per_km=gas_per_km
        self.distride=distride

    def fill (self, amt):
        if amt > self.capacity - self.gas:
            self.gas = self.capacity
            print("Full and", amt + self.gas - self.capacity, "lishnih litrov")
        else:
            self.gas=self.gas+amt


    def ride (self, dist):
        if dist > self.gas * self.gas_per_km:
            self.gas = 0
            self.distride += self.gas / self.gas_per_km
            print("Bak pust! Proehali", self.gas / self.gas_per_km, "kilometrov")
        else:
            self.gas=self.gas - dist * self.gas_per_km
            self.distride += dist * self.gas_per_km
            print("Proehali", dist * self.gas_per_km, "kilometrov")

car1 = Car('6ka', 3, 30, 2, 200000)
car2 = Car('Lada',5, 35, 3,100000)
car3 = Car('Hammer', 40,60,10, 10)

print(car1.fill(20), car1.gas, car1.distride)
print(car1.fill(20), car1.gas, car1.distride)
print(car1.ride(30), car1.gas, car1.distride)

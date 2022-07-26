class Car:
    def __init__(self, capacity, gas_per_km):
        self.gas = 0
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.adometr = 0

    def fill(self, litr):
        if self.gas + litr > self.capacity:
            outfill = self.gas + litr - self.capacity
            self.gas = self.capacity
            print(f"В бак не влезло {outfill} литров")
        else:
            self.gas += litr

    def ride(self, km):
        available_km = self.gas / self.gas_per_km
        if available_km >= km:
            print(f"проехали {km} километров")
            self.gas -= self.gas_per_km * km
            self.adometr += km
        else:
            print(f"проехали {available_km} километров")
            self.gas -= self.gas_per_km * available_km
            self.adometr += available_km


car1 = Car(capacity=100, gas_per_km=.1)
car1.fill(50)
car1.ride(100)
car1.fill(100)
car1.ride(1000)
print(car1.adometr)

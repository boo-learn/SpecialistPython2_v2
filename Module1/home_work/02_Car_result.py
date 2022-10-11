
class Car:

    def __init__(self, gas, capacity, gas_per_km):
        self.probeg = 0
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km


    def fill(self, litres):
        if self.gas + litres > self.capacity:
            print(f'Лишние {self.gas + litres - self.capacity} литров')
            self.gas = self.capacity
        else:
            self.gas += litres


    def ride(self, way):
        if self.gas > way*self.gas_per_km:
           self.gas = self.gas - way*self.gas_per_km
           print(f'Проехали {way} километров')
           self.probeg += way
        else:
           print(f'На {way} километров бензина не хватит')



vesta = Car(10, 50, 0.09)
vesta.ride(200)
print(vesta.__dict__)
vesta.fill(60)
print(vesta.__dict__)


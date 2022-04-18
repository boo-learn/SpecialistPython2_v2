class Car:
    def __init__(self, gas, capasity, gas_per_km, probeg=0):
        if gas > capasity: gas = capasity
        self.gas = gas
        self.capasity = capasity
        self.gas_per_km = gas_per_km
        self.probeg = probeg

    def fill(self, gas_to_fill):
        self.gas += gas_to_fill
        if self.gas + gas_to_fill > self.capasity:
            print(f"в бак не влезло {self.gas - self.capasity} литров")
            self.gas = self.capasity

    def ride(self, range):
        if range < (self.gas / self.gas_per_km * 100):
            print(f"бензина хватает на все {range}км")
            self.probeg += range
            self.fill(range / 100 * self.gas_per_km * -1)
        else:
            print(f"проехали {self.gas / self.gas_per_km * 100}км \n"
                  f"на остальные {range - self.gas / self.gas_per_km * 100} бензина не хватит")
            self.probeg += self.gas / self.gas_per_km * 100
            self.gas = 0


car1 = Car(30, 50, 7)
car1.fill(50)
print(f"в баке залито {car1.gas}л")
car1.ride(700)
print(f"в баке залито {car1.gas}л")
print(f"пробег машины составляет {car1.probeg}км")

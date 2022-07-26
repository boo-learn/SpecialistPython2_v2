class Car:
    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0


    def fill(self, liters):
        if (liters + self.gas) > self.capacity:
            print ( f'Залили бак полностью. Осталось лишних {liters + self.gas - self.capacity} литров' )
            self.gas = self.capacity
        else:
            self.gas += liters

    def ride(self, km):

        init_gas = self.gas
        self.gas -= km * self.gas_per_km

        if self.gas < 0:
            print(f'Бензин закончился. Удалось проехать лишь {init_gas * self.gas_per_km} километров')
            self.mileage = self.mileage + init_gas * self.gas_per_km
            self.gas = 0
        else:
            print(f'Проехали {km} километров, потратили {km * self.gas_per_km} литров топлива')
            self.mileage = self.mileage + km * self.gas_per_km

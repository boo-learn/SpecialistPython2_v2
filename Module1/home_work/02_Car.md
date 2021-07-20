class Car:
    def __init__(self, gas, capacity, gas_per_km, run):
        self.gas = gas #сколько бензина в баке
        self._capacity = capacity #вместимость бака
        self.gas_per_km = gas_per_km #расход топлива на км
        self.run = run #пробег

    count = 0

    def fill(self, prihod):
        if self.gas + prihod <= self._capacity:
            self.gas += prihod
        else:
            print(f'Налито на {self.gas + prihod - self._capacity} литров больше')
            self.gas = self._capacity
        return self.gas

    def ride(self, dist):
        if self.gas_per_km * dist <= self.gas:
            print(f'Проехали {dist} километров')
            self.gas = self.gas - self.gas_per_km * dist
            self.run += dist
            Car.count += dist
        else:
            distance = self.gas / self.gas_per_km
            print(f'Проехали {distance} километров')
            self.run += distance
            self.gas = 0
            Car.count += distance
        if Car.count >= 1000:
            Car.count = Car.count - 1000
            self.gas_per_km = self.gas_per_km * 1.05

class Car:
    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.distance = 0
        
    def fill(self, x):
        self.gas += x 
        if self.gas > self.capacity:
            self.gas = self.capacity
            print ('Количество заливаемых литров превышает вместимость бака')
            
    def ride(self, x):
        new_gas = self.gas - self.gas_per_km * x 
        if new_gas < 0:
            dist_ = self.gas / self.gas_per_km
            self.distance += dist_
            message = f'проехали {dist_} километров'
            self.gas_per_km += self.gas_per_km * (dist_/ 1000 * 0.05)
            self.gas = 0
        else:
            self.distance += x
            message = f'проехали {x} километров'
            self.gas_per_km += self.gas_per_km * (x/ 1000 * 0.05)
            self.gas = self.gas - self.gas_per_km * x
        return message

class Car:

    def __init__(self, gas, capacity, gas_per_km, race=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.race = race
        self.current_gas_per_km = gas_per_km

    def fill(self, litres):
        if litres > (self.capacity - self.gas):
            self.gas = self.capacity
            print('There is not enough space')
        else:
            self.gas += litres
    
    def ride(self, distance):
        # Я запуталась, как использовать здесь интеграл
        to_ride = distance
        while self.gas > 0 and distance > 0:
            self.gas -= self.current_gas_per_km
            self.race += 1
            distance -= 1
            self.update_gas_per_km()
        print(f'We have drove {to_ride - distance} km')

    def update_gas_per_km(self):
        self.current_gas_per_km = self.gas_per_km * (1.05 ** (self.race / 1000))

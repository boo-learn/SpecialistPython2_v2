class Car:
    def __init__(self, gas, capacity, gas_per_km, milage):
        self.gas = gas  # Сколько бензина в баке
        self.capacity = capacity  # Вместимость бака
        self.gas_per_km = gas_per_km  # Расход топлива на км
        self.milage = milage  # Пробег машины

    def fill(self, petrol):
        self.gas += petrol
        if self.gas > self.capacity:
            extra_liters = self.gas - self.capacity
            self.gas = self.capacity
            print(f'Не влезло в бак {extra_liters} литров')

    def ride(self, ride_km):
        temp_ride_km = ride_km
        while self.gas >= self.gas_per_km and temp_ride_km > 0:
            self.gas -= self.gas_per_km
            temp_ride_km -= 1
            self.milage += 1
        if temp_ride_km == 0:
            print(f'Проехали {ride_km} километров')
        else:
            print(f'Проехали {ride_km - temp_ride_km} километров, кончился бензин')
        print(f'Пробег машины {self.milage}')


car1 = Car(14, 15, 5, 16)

car1.fill(5)
car1.ride(50)

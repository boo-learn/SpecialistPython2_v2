class Car:

    def __init__(self, capacity, gas_per_km, gas=0):
        self.gas = gas                  # сколько бензина в баке (литр)
        self.capacity = capacity        # вместимость бака (литр)
        self.gas_per_km = gas_per_km    # расход топлива на один километр (литр/км)
        self.mileage = 0

    def fill(self, add_gas):
        if self.gas + add_gas > self.capacity:
            print(f"Бак полон! Перелив составил {self.gas + add_gas - self.capacity} литров!")
            self.gas = self.capacity
        else:
            self.gas += add_gas

    def ride(self, ride_distance):
        if ride_distance * self.gas_per_km < self.gas:
            self.mileage += ride_distance
            self.gas -= ride_distance * self.gas_per_km
        else:
            self.mileage += ride_distance
            print("У машины закончилось топливо!")
            self.gas = 0

    def specifications(self):
        print(f"  # Capacity: {self.capacity} / Gas_per_km: {self.gas_per_km} "
              f"/ Gas: {self.gas:.02f} / Mileage: {self.mileage}")
        print()


ferrari = Car(60, 0.1)
ferrari.specifications()

print("Заправляем на 30 литров")
ferrari.fill(30)
ferrari.specifications()

print("Заправляем на 40 литров")
ferrari.fill(40)
ferrari.specifications()

print("Едем 100 км")
ferrari.ride(100)
ferrari.specifications()

print("Едем ещё 499 км")
ferrari.ride(499)
ferrari.specifications()

print("Едем ещё 10 км")
ferrari.ride(499)
ferrari.specifications()

print("Заправляем на 30 литров")
ferrari.fill(30)
ferrari.specifications()

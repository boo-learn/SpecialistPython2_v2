class Car:
    def __init__(self, V_bac, gas, gas_per_km, mileage):
        self.V_bac = V_bac
        self.gas = gas
        self.gas_per_km = gas_per_km
        self.mileage = mileage

    def fill(self, add_gas):
        if self.V_bac - self.gas >= add_gas:
            print(f'Заправлено литров {add_gas}')
        else:
            print(f'Заправлено литров - {self.V_bac - self.gas}\n'
                  f'Лишние литры - {add_gas - (self.V_bac - self.gas)}')

    def ride(self, ride_KM):
        if ride_KM <= self.gas/self.gas_per_km:
            print(f'проехали {ride_KM/self.gas_per_km} километров')
            self.mileage += ride_KM/self.gas_per_km
        else:
            print(f'проехали {self.gas/self.gas_per_km} километров, бензин кончился, не доехали - {ride_KM - self.gas/self.gas_per_km} километров')
            self.mileage += self.gas/self.gas_per_km

    def info(self):
        print(f'info: {self.mileage}')


car1 = Car(60, 30, 1, 500)

print(car1.fill(30))
print(car1.ride(40))
print(car1.info())

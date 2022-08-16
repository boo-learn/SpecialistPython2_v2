class Car:
    def __init__(self, gas, capicity, gas_per_km, total_ride):
        self.gas = gas
        self.capicity = capicity
        self.gas_per_km = gas_per_km
        self.total_ride = total_ride

    # def show_gas(self):
    #     print(self.gas)

    # def show_total_ride(self):
    #     print(self.total_ride)

    def fill(self, f):
        if f + self.gas <= self.capicity:
            self.gas += f
        else:            
            print('Лишние литры: ', (f + self.gas) - self.capicity)
            self.gas = self.capicity

    def ride(self, r):
        gas_consup = r / self.gas_per_km
        if gas_consup <= self.gas:
            print('Пройденное расстояние: ', r, ', ',  'расход: ', round(gas_consup, 1), sep = '')
            self.total_ride += r
        else:
            print('Проехали всего: ', self.gas * self.gas_per_km)
            self.total_ride += self.gas * self.gas_per_km
  
car1 = Car(10, 70, 7, 10)

car1.fill(65)

# car1.show_gas()

car1.ride(700)

# car1.show_total_ride()

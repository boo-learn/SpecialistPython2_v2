class Car:
    def __init__(self, gas: int , capacity: int , gas_per_km: int, mileage:int = 0 ):
        self.gas = gas #сколько бензина в баке
        self.capacity = capacity #вместимость бака
        self.gas_per_km = gas_per_km #расход топлива на км
        self.mileage = mileage #Пробег

    def fill(self, amount:int):
        free_gas = self.capacity - self.gas
        if free_gas >= amount:
            self.gas += amount
            print('Заправились на ' + str(amount) + 'л')
            print('В баке ' + str(self.gas) + 'л')
        else:
            self.gas += free_gas
            print('Заправились на ' + str(amount) + 'л')
            print('Лишнее: ', amount - free_gas)

    
    def ride(self, want_ride: int):
        can_ride = self.gas / self.gas_per_km
        if want_ride >= can_ride:
            self.gas = 0
            self.mileage += can_ride
            print('Проехали '+ str(can_ride) +' km')
            print('Бензин закончился')

        else:
            self.gas -= self.gas_per_km * want_ride
            self.mileage += want_ride
            print('Проехали '+ str(want_ride) +' km')
            print('Осталось ' + str(self.gas) + 'л бензина' )
      

car1=Car(25,50,1)        
car1.fill(100)
car1.ride(44)
car1.ride(2)
print(car1.mileage)

class Car:

    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas #сколько бензина в баке
        self.capacity = capacity #вместимость бака
        self.gas_per_km = gas_per_km #расход топлива на 100 км
   
    def fill(self, gas_fill):
        gas_def = self.capacity - self.gas
        if gas_fill > gas_def:
            self.gas = self.capacity
            print(f'Машина заполнена полностью, не стоит вливать {gas_fill - gas_def} лишних литров')
            return self.gas
        elif gas_fill == gas_def:
            self.gas = self.capacity
            print('Машина заполнена полностью')
            return self.gas
        else:
            self.gas = self.gas + gas_fill
            print(f'Машина заполнена на {self.gas} литр(ов)')
            return self.gas
    
    def ride(self, ride_km):
         gas_ride = ride_km * self.gas_per_km / 100
         if gas_ride < self.gas:
             print(f'Проехали {ride_km} километров. Осталось бензина ->{self.gas - gas_ride} л ')
         elif gas_ride == self.gas:
             print(f'Проехали {ride_km} километров. К сожалению бензина не осталось')
         else:
             print(f'Проехали {self.gas * 100 / self.gas_per_km} километров. К сожалению бензина не осталось. Осталось проехать {ride_km - self.gas * 100 / self.gas_per_km} км')
    
car1 = Car(0, 60, 12)
car1.fill(60)
car1.ride(1200)

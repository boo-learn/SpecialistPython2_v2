class Car:
    def __init__(self, gas, capasity, gas_per_km, probeg):
        self.gas = gas
        self.capasity = capasity 
        self.gas_per_km = gas_per_km
        self.probeg = probeg
        
    def fill(self, zapr):
        if self.gas + zapr > self.capasity:
            self.gas = zapr
            print(f"Бак заполнен полностью, {zapr + self.gas - self.capasity} литров в канистру")
        else:
            self.gas += zapr
            
    def ride(self, km):
        if self.gas_per_km * km < self.gas:
            self.gas -= self.gas_per_km * km
            self.probeg =+ km
            print(f"Проехали {km} километров") 
        elif self.gas == 0:
            print("Бензина нет, упс")      
        else:
            loser = int(self.gas/self.gas_per_km)
            self.gas = 0
            self.probeg += loser
            print(f"Топаем до заправки пешочком, проехали {loser} километров, бенз кончился")

         
car1 = Car(20,63,3,0) 
car1.fill(50)    
car1.ride(20)   
car1.ride(10)
print(car1.probeg)

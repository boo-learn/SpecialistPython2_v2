class Car:
    def __init__(self, gas: int , capacity: int , gas_per_km: int):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km # for 100 km
        self.mileage = 0 # new car)
    
    def fill(self, volume: int):
        if volume <= self.capacity - self.gas:
            self.gas += volume
            return print(f"Машина заправлена. В баке ({self.gas})")
        elif volume > self.capacity - self.gas:
            over = volume - (self.capacity - self.gas) 
            self.gas = self.capacity
            return print(f"Машина заправлена до полного бака({self.capacity}) и осталось лишние ({over})")
    
    def ride(self, dist: int):
        gas_need = dist*10/100
        if self.gas > gas_need:
            self.gas -= gas_need
            self.mileage += dist
            return print(f"Машина проехала {dist}км в баке осталось ({self.gas}) пробег {self.mileage}км")
        elif self.gas == gas_need:
            self.gas -= gas_need
            self.mileage += dist
            return print(f"Машина проехала {dist}км в баке осталось ({self.gas}) пробег {self.mileage}км")
        elif self.gas == 0:
            return print("В баке нет бензина, мы не можем ехать!")
        elif self.gas < gas_need:
            dist = self.gas / self.gas_per_km * 100
            self.gas = 0
            self.mileage += dist
            return print(f"Машина проехала {dist}км в баке осталось ({self.gas}) пробег {self.mileage}км")
        
        
audi = Car(25,50,10)
audi.ride(15)
audi.ride(123)
audi.ride(32)
audi.fill(423)
audi.ride(1253)

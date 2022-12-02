class Car:
    """Класс машины"""
    def __init__(self, gas: float, capacity: int, gas_per_km: float):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.traveled = 0


    def fill(self, fill_the_car: float) -> float:
        """Заправка машины в литрах."""
        if self.gas == 50:
            return 'Полный бак.'
        elif fill_the_car > self.capacity - self.gas:
            too_much = fill_the_car - self.gas
            self.gas = self.capacity
            return f'Полный бак. Вы пытались заправить на {too_much} литров больше'
        else:
            self.gas += fill_the_car
            return f'После заправки в баке {self.gas} литров'        


    def ride(self, ride_km: float) -> float:
        """Движение автомобиля в км."""
        if ride_km * self.gas_per_km > self.gas:
            return 'Топлива не хватит!'
        else:
            self.gas = self.gas - ride_km * self.gas_per_km
            self.traveled += ride_km
            return f'Проехали {ride_km} км. Всего проехали {self.traveled} км'
    
car1 = Car(20.5, 50, 0.1)

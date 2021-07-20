class Car:
    """
    Класс Car - характеристики автомобиля, заправка, поездка.
    
    Атрибуты:
    gas - текущий уровень топлива, л.
    capacity - емкость топливного бака, л.
    gas_per_km - текущий уровень расхода топлива (л./1км.)
    mileage - общий пробег автомобиля
    
    Методы:
    fill() - заправить автомобиль указанным количеством топлива (л.), индикация полного бака
    ride() - проехать указанный путь (км.), индикация пустого бака
    """

    def __init__(self, gas, capacity, gas_per_km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = mileage

    def fill(self, fuel: float):
        if fuel > (self.capacity - self.gas):
            self.gas = self.capacity
            print('заправили до полного бака, оплачено лишних', (fuel - (self.capacity - self.gas)) , 'литров')
        else:
            self.gas += fuel
            print('заправили на', fuel, 'литров')

    def ride(self, distance: float):
        if distance > (self.gas / self.gas_per_km):
            print('Проехали', (self.gas / self.gas_per_km), 'км, кончился бензин')
            self.mileage += self.gas / self.gas_per_km
            self.gas = 0
        else:
            print('Проехали', distance, 'км')
            self.mileage += distance
        self.gas_per_km += self.gas_per_km * (0.05 * (distance / 1000))

car1 = Car(10, 50, 0.1, 30000) # автомобиль №1
car1.fill(30) # пример заправки на 30л
car1.ride(50) # пример поездки на 50км
print('Остаток бензина в автомобиле №1 после поездки:',car1.gas , 'л.')
print('Общий пробег автомобиля №1 после поездки:', car1.mileage, 'км.')
print('Текущий расход топлива автомобиля №1:', round(car1.gas_per_km, 4), 'л. на один км.')

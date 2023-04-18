# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md
class Car:
    def __init__(self, capacity, gas_per_km):
        self.gas = 0
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0

    def fill(self, litres) -> None:
        if self.gas == self.capacity:
            print(f'Gas tank is full! {self.gas} litres')
        elif self.gas + litres > self.capacity:
            difference = self.gas + litres - self.capacity
            self.gas = self.capacity
            print(f'Gas tank is full! {self.gas} litres. {difference} litres not fitted in')
        elif self.gas + litres == self.capacity:
            self.gas = self.capacity
            print(f'Gas tank is full! {self.gas} litres')
        else:
            self.gas += litres
            print(f'{self.gas} litres')

    def ride(self, distance) -> None:
        if distance * self.gas_per_km > self.gas:
            actual_distance = self.gas / self.gas_per_km
            self.mileage += actual_distance
            self.gas = 0
            print(f'ride summary:\nactual ride distance: {actual_distance} km\ngas left: {self.gas} litres'
                  f'\nmileage: {self.mileage} km')
            print('gas tank is empty, please fill!')
        else:
            self.gas -= distance * self.gas_per_km
            self.mileage += distance
            print(f'ride summary:\nactual ride distance: {distance} km\ngas left: {self.gas} litres'
                  f'\nmileage: {self.mileage} km')


print('Lets take a car!')
car1 = Car(int(input('enter gas tank capacity: ')), int(input('enter gas consumption per km: ')))
while True:
    action = input('refill gas tank (re) or ride (ri)?: ')
    if action == 're':
        litres = int(input('How much litres?: '))
        car1.fill(litres)
    if action == 'ri':
        distance = int(input('How much kilometers?: '))
        car1.ride(distance)

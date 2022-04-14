class Car:
    def __init__(self, name, gas, capacity, gas_per_km, mileage=0):
        self.name = name
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = mileage

    def fill(self, volume):
        if volume >= 0:
            if volume > self.capacity - self.gas:
                print(f'{volume - (self.capacity - self.gas)} литров не вместилось в бак.')
                self.gas = self.capacity
            else:
                self.gas += volume
        else:
            print('Вы ввели некорректное значение.')

    def ride(self, path):
        fuel_dist = self.gas / self.gas_per_km
        if path >= 0:
            if fuel_dist >= path:
                self.mileage += path
                self.gas -= path * self.gas_per_km
                print(f'Вы проехали {path} км.')
            else:
                self.mileage += fuel_dist
                self.gas = 0
                print(f'Вам не хватило бензина. Вы проехали {fuel_dist} км.')
        else:
            print('Вы ввели некорректное значение.')


# вспомогательная функция
def show_car(car):
    return f"{car.name} {car.gas} {car.capacity} {car.gas_per_km} {car.mileage}"

car = Car('Ford', 10, 60, 0.5)

print(show_car(car))

volume = float(input('Сколько литров Вы хотите залить? '))
car.fill(volume)

print(show_car(car))

path = float(input('Сколько километров Вы хотите проехать? '))
car.ride(path)

print(show_car(car))

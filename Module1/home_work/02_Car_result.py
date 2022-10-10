# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, capacity, gas_per_km, run) -> None:
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.run = run

    def fill(self, fill_gas):
        if self.gas + fill_gas > self.capacity:
            print(f'Лишних литров : {(self.gas + fill_gas) - self.capacity}')
            self.gas = self.capacity
        else:
            self.gas += fill_gas

    def ride(self, km):
        if self.gas < self.gas_per_km * km:
            ride_km = int(self.gas / self.gas_per_km)
            print(f'Проехали {ride_km} километров и остановились')
            self.gas = 0
            self.run += ride_km
        else:
            print(f'Проехали {km} километров')
            self.gas -= km*self.gas_per_km
            self.run += int(km)


if __name__ == '__main__':
    Car1 = Car(0, 15, 1, 0)
    Car1.fill(20)
    Car1.ride(10)
    print(Car1.gas, Car1.capacity, Car1.gas_per_km, Car1.run)
    Car1.ride(15)
    print(Car1.gas, Car1.capacity, Car1.gas_per_km, Car1.run)

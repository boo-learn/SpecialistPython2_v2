# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas: int, capacity: int, gas_per_km: float, mileage: int) -> None:
        self.gas = gas                      # сколько бензина в баке
        self.capacity = capacity            # вместимость бака" - сколько максимум вмещается бензина (capacity)
        self.gas_per_km = gas_per_km        # расход топлива на км" (gas_per_km)
        self.mileage = mileage              # атрибут с пробегом, который увеличивается в результате ride

    def fill(self, pour_gas):
        if (self.gas + pour_gas) > self.capacity:
            self.gas = self.capacity
            print('Бак полон. Лишних литров {}'.format(self.gas + pour_gas - self.capacity))
        else: 
            print('Залили {} литров бензина. В баке {} литров бензина.'.format(pour_gas, (self.gas + pour_gas)))
            self.gas = self.gas + pour_gas

    def ride(self, ride_distance):
        if self.gas_per_km * ride_distance <= self.gas:
            print('Машина проехала {} км. и потратила {} литров бензина'.format(ride_distance, (self.gas_per_km * ride_distance)))
            self.mileage += ride_distance
            self.gas = round(self.gas - self.gas_per_km * ride_distance, 2)         # Сколько осталось бензина
        else:
            print('Машина не проехала {} км. так как не хватило бензина. Машина смогла проехать {:.2f} км. и потратила весь бензин {} в баке'.format(ride_distance, round(self.gas / self.gas_per_km, 2), self.gas))
            self.mileage += round(self.gas / self.gas_per_km, 2)
            self.gas = 0                                                    # Сколько осталось бензина
        

car1 = Car(2, 65, 0.12, 123432)
car1.fill(5)
print(car1.mileage)
print(car1.gas)
car1.ride(57)
print(car1.mileage)
print(car1.gas)

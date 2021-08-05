## Автомобиль

Описать класс Car
``` python
class Car:
  ...
  
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на км" (gas_per_km)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```

должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью + print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```

выведет сообщение "проехали ... километров"
в результате поездки потратится бензин
Машина едет пока хватает бензина

г) добавить атрибут с пробегом, который увеличивается в результате ride

★д) сделать так, чтобы расход топлива увеличивался на 5% каждые 1000км.
*Здесь можно либо увеличивать пробег скачкообразно каждые 1000км, можно увеличивать более плавно каждый км, а можно вспомнить школьные интегралы.*

class Car:
    def __init__(self, name: str, gas_tank: int, per_km: int):
        self.name = name
        self.gas_tank = gas_tank
        self.per_km = per_km
        self.gas = 0
        self.mileage = 0
        self.wear = 0

    def fill(self, fuel: int):
        if self.gas_tank > self.gas + fuel:
            self.gas += fuel
            return f'Машина заправлена. {self.gas} литров в баке'
        else:
            max_to_fill = self.gas_tank - self.gas
            excess_fuel = fuel - max_to_fill
            self.gas = 50
            return f'Машина заправлена до полного бака. Заправленно {fuel} литров. Лишних {excess_fuel}.'

    def ride(self, km: int):
        spend = km * self.per_km
        if self.gas - spend > 0:
            self.gas -= spend
            self.mileage += km
            self.engine_wear(km)
            return f'Проехали {km} километров. Потрачено {spend:.0f} литров бензина. Осталось {self.gas:.0f} топлива.'
        else:
            overrun = spend - self.gas
            spend -= overrun
            new_km = round(spend / self.per_km)
            self.mileage += new_km
            self.gas = 0
            self.engine_wear(new_km)
            return f'Проехли {new_km} километров. Бак пуст. Не хватило топлива что проехать остальные {round(overrun / self.per_km)} километров'

    def engine_wear(self, km):
        self.wear += km
        while self.wear >= 1000:
            self.per_km *= 1.05
            self.wear -= 1000

my_little_car = Car('lada', 50, 5)

print(my_little_car.name, my_little_car.gas_tank)
print(my_little_car.fill(30))
print(my_little_car.fill(30))

print(my_little_car.ride(5))
print(my_little_car.ride(3))
print(my_little_car.ride(10))

print(my_little_car.fill(30))
print(my_little_car.fill(20))

print(my_little_car.mileage)
my_little_car.engine_wear(5000)
print(my_little_car.mileage)

print(my_little_car.ride(5))
print(my_little_car.ride(3))
print(my_little_car.ride(10))

print(my_little_car.fill(30))
print(my_little_car.fill(30))

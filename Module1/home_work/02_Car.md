## Автомобиль

Описать класс Car
``` python
class Car:

    def __init__(self, gas, capacity, gas_per_km, race=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.race = race
        self.current_gas_per_km = gas_per_km

    def fill(self, litres):
        if litres > (self.capacity - self.gas):
            self.gas = self.capacity
            print('There is not enough space')
        else:
            self.gas += litres
    
    def ride(self, distance):
        max_distance = self.gas / self.current_gas_per_km
        real_distance = (max_distance, distance)[distance < max_distance]
        self.gas -= self.current_gas_per_km * real_distance
        self.update_gas_per_km()
        print(f'We have drove {real_distance} km')

    def update_gas_per_km(self):
        # Я предположила, что механизм будет подобен начислению сложных процентов
        self.current_gas_per_km = self.gas_per_km * (1.05 ** (self.race / 1000))

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

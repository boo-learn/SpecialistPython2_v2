# Описать класс Автомобиль:
    # а) У машины должны быть атрибуты:
        # "сколько бензина в баке" (gas);
        # "вместимость бака" - сколько максимум вмещается бензина (capacity)
        # "расход топлива на км" (gas_per_km)
    # б) метод "залить столько-то литров в бак":
        # должна учитываться вместительность бака если пытаемся залить больше, чем вмещается,
        # то заполняется полностью + print'ом выводится сообщение о лишних литрах
    # в) метод "проехать сколько-то км":
        # выведите сообщение: "проехали ... километров" в результате поездки тратится бензин.
        # Машина едет пока хватает бензина.
    # г) добавить атрибут с пробегом, который увеличивается в результате ride
    
class Car:
    def __init__(self, gas, capacity, gas_per_km, run):
        self.gas = gas
        self.capacity = capacity
        self.gas_km = gas_per_km
        self.run = run
    
    def fill(self, liters):
        self.liters = liters
        fill_gas = self.gas + liters
        if fill_gas > self.capacity:
            excess = fill_gas - self.capacity
            self.gas = self.capacity
            excess_line = f'Лишних литров: {excess}.'
        else:
            self.gas += liters
            excess_line = ''
        return excess_line
        
    def ride(self, km):
        self.km = km
        can_run_km = self.gas / self.gas_km
        if can_run_km > self.km:
            can_run_km = self.km
        self.run += round(can_run_km, 2)
        spent_gas = int(can_run_km * self.gas_km)
        self.gas -= spent_gas
        return round(can_run_km, 2)
    
def ending(num):
    end = 'ов'
    if num % 100 < 5 or  num % 100 > 14:
        if num % 10 > 1 and num % 10 < 5:
            end = 'а'
        if num == 0:
            end = ''
    return end

car1 = Car(2, 50, 1.8, 78)
print(f'Есть машина car1 с вместимостью бака {car1.capacity} лирт{ending(car1.capacity)} \
и пробегом {car1.run} километр{ending(car1.run)}.\n\
Расход топлива на киллометр составляет: {car1.gas_km} литра.\n\
Сначала бензина в баке было {car1.gas} лирт{ending(car1.gas)}.')
car_fill = car1.fill(5)  # залили 5 литров
print(f'Долили {car1.liters} лирт{ending(car1.liters)}. {car_fill}')
car_ride = car1.ride(50)  # едем 50 км (если хватит топлива)
print(f'Проехали {car_ride} километр{ending(car_ride)}.\n\
Теперь пробег машины {car1.run} километр{ending(car1.run)}, \
а бензина в баке {car1.gas} лирт{ending(car1.gas)}.')

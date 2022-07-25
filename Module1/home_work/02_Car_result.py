# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md
import math


class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.__mileage = mileage
        if gas_per_km <= 0:
            print("Вы случайно изобрели Perpetum mobile!")  # raiseerror!

    def fill(self, gas_amount):
        if self.gas + gas_amount > self.capacity:
            print(f"Куда столько льёшь?!")
            self.gas = self.capacity
        elif gas_amount < 0:
            print(f"Топливо сливают!")
        elif gas_amount == 0:
            print(f"Ну, может что-нибудь нальёшь?")
        else:
            self.gas += gas_amount
        print(f"Заправились. В баке теперь {self.gas} л")

    def calc_fuel_distance(self):
        if self.gas_per_km <= 0:
            return -1
        else:
            return math.floor(self.gas*100 / self.gas_per_km)

    # MILEAGE
    def __increase_mileage(self, incr):
        self.__mileage += incr

    def __set_mileage(self, value):
        self.__mileage = value

    def get_mileage(self):
        return self.__mileage

    def ride(self, distance):
        if self.calc_fuel_distance() >= distance:
            self.__increase_mileage(distance)
            self.gas -= distance/100 * self.gas_per_km
            print(f"{self.__kilometrs_ride_spelling(distance)} км. В баке осталось {self.gas} л")
            return distance
        else:
            _calc = self.calc_fuel_distance()
            self.__increase_mileage(_calc)
            self.gas = 0
            print(f"{self.__kilometrs_ride_spelling(_calc)} км. В баке осталось {self.gas} л")
            return _calc

    def __kilometrs_ride_spelling(self, km):
        km_spelling_dict=""
        match km % 10:
            case 1:
                km_spelling_dict = 'километр'
            case 2:
                km_spelling_dict = 'километра'
            case 3:
                km_spelling_dict = 'километра'
            case 4:
                km_spelling_dict = 'километра'
            case 5:
                km_spelling_dict = 'километров'
            case 6:
                km_spelling_dict = 'километров'
            case 7:
                km_spelling_dict = 'километров'
            case 8:
                km_spelling_dict = 'километров'
            case 9:
                km_spelling_dict = 'километров'
            case 0:
                km_spelling_dict = 'километров'

        return "проехали " + str(km) + " " + km_spelling_dict

    def show_kilometrs_ride_spelling(self, _km):
        print(self.__kilometrs_ride_spelling(_km))


# create auto
lada_granta = Car(gas=15, capacity=50, gas_per_km=7.5, mileage=89999)

# lada_granta.show_kilometrs_ride_spelling(30)
# lada_granta.show_kilometrs_ride_spelling(41)
# lada_granta.show_kilometrs_ride_spelling(52)
# lada_granta.show_kilometrs_ride_spelling(63)
# lada_granta.show_kilometrs_ride_spelling(74)

print(f'mileage of lada_granta is {str(lada_granta.get_mileage())}')

probeg = 10000
print(f'Now we wanna ride about {probeg} km and could reach {lada_granta.ride(distance=probeg)} km radius')

lada_granta.fill(300)
probeg = 5000
print(f'Now we wanna ride about {probeg} km and could reach {lada_granta.ride(distance=probeg)} km radius')

lada_granta.fill(50)
probeg = 500
print(f'Now we wanna ride about {probeg} km and could reach {lada_granta.ride(distance=probeg)} km radius')

lada_granta.fill(0)

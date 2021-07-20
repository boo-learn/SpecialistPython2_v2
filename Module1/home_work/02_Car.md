# Автомобиль
# Описать класс Car
# а) У машины должны быть атрибуты
#     "сколько бензина в баке" (gas)
#     "вместимость бака" - сколько максимум влезаем бензина (capacity)
#     "расход топлива на км" (gas_per_km)
# б) метод "залить столько-то литров в бак"
# car1.fill(5)  # залили 5 литров
# должна учитываться вместительность бака если пытаемся залить больше, чем вмещается, то заполняется полностью + print'ом выводится сообщение о лишних литрах
# в) метод "проехать сколько-то км"
# car1.ride(50)  # едем 50 км (если хватит топлива)
# выведет сообщение "проехали ... километров" в результате поездки потратится бензин Машина едет пока хватает бензина
# г) добавить атрибут с пробегом, который увеличивается в результате ride
# ★д) сделать так, чтобы расход топлива увеличивался на 5% каждые 1000км. Здесь можно либо увеличивать пробег
# скачкообразно каждые 1000км, можно увеличивать более плавно каждый км, а можно вспомнить школьные интегралы.

class Car:
    def __init__ (self,gas,capacity,gas_per_km):
        self.gas=gas
        self.capacity=capacity
        self.gas_per_km=gas_per_km
        self.ride_km=0

    def full(self, n):
        if self.gas+n>self.capacity:
            print("Бак заполнен полностью, лишние литры:", n-self.capacity + self.gas, "л.")
            self.gas=self.capacity
        else:
            self.gas=self.gas+n
        return
    def ride(self, km):
        if self.gas_per_km*km<=self.gas:
            print("Проехали", km, "км")
            self.gas=self.gas-self.gas_per_km*km
            self.ride_km=self.ride_km+km
        else:
            print("Проехали", self.gas//self.gas_per_km, "км")
            self.gas = self.gas%self.gas_per_km
            self.ride_km = self.ride_km+ self.gas//self.gas_per_km


car1 = Car(10,100,3)
car1.full(150)
car1.ride(20)

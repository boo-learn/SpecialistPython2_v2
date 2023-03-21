# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, max_capacity):
        self.gas = 0
        self.total = 0
        self.max_capacity = max_capacity

    def fill(self, liters):
        if self.gas + liters <= self.max_capacity:
            self.gas += liters
            print(f"Заправили {liters}")
        else:
            over = self.gas + liters - self.max_capacity
            self.gas += liters - over
            print(f"Заправили {liters}, лишние {over}")
    
    def add_kilometers(self, km):
        self.total += km

    def ride(self, distance):
        if self.gas == 0:
            print(f"Бак пустой")
        else: 
            if distance <= self.gas:
                self.gas -= distance
                self.add_kilometers(distance)
                print(f'Проехали {distance} км, топлива осталось {self.gas}')
            else:
                 print(f'Хвататет только на {self.gas} км')
    


car = Car(50)

car.fill(40)
car.fill(20)

car.ride(20)
car.ride(20)
print("Вcего проехали", car.total)
car.ride(15)
car.fill(10)
car.ride(20)
car.ride(20)
print("Вcего проехали", car.total)
car.ride(5)
car.ride(20)




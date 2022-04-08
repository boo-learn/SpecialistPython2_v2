# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas:float=0, capacity:int=5, gas_per_kilometer:float=0.1, riding:float=0 ):
        self.gas = gas
        self.gas_per_kilometer = gas_per_kilometer
        self.capacity = capacity
        self.riding = riding

    def fill(self, gas):
        if self.gas + gas <= self.capacity:
            self.gas += gas
        else:
            print(f"{gas - (self.capacity - self.gas)} литров бензина лишние")
            self.gas = self.capacity

    def ride(self, km):
        gas = km * self.gas_per_kilometer
        if gas > self.gas:
            km = self.gas / self.gas_per_kilometer
        if km > 0:
            self.riding += km
            self.gas -= km * self.gas_per_kilometer
            print(f"Проехали {km} км")
        else:
            print("Стоим, нет бензина")


if __name__ == "__main__":
    car = Car(gas=1, capacity=10)
    car.fill(9)
    car.ride(50)
    car.ride(40)
    car.ride(10)
    car.ride(1)
    car.ride(10)
    car.fill(5)
    car.ride(10)
    print(car.riding)


class Car:
    """
    Класс "Автомобиль"
    """

    def __init__(self, g=0, c=40, gpkm=0.1, mileage=0):
        self.gas = g  # сколько бензина в баке
        self.capacity = c  # вместимость бака - сколько максимум вмещается бензина
        self.gas_per_km = gpkm  # расход топлива на км
        self.mileage = mileage  # пробег

    def fill(self, gas):
        """
        Метод "залить столько-то литров в бак"
        """
        self.gas += gas
        if self.gas > self.capacity:
            gas = self.gas - self.capacity
            self.gas = self.capacity
            print(f"Залили полный бак. Осталось {gas} л бензина")

    def ride(self, path_length):
        """
        Метод "проехать сколько-то км"
        """
        potential = self.gas / self.gas_per_km  # можно проехать без заправки
        if potential >= path_length:
            print(f"проехали {path_length} километров")
            self.gas -= path_length * self.gas_per_km  # остаток бензина в баке
            self.mileage += path_length  # пробег
        else:
            print(f"проехали {potential} километров (из {path_length})")
            self.gas -= 0  # бак пуст
            self.mileage += potential  # пробег


# car1 = Car(20, 40, 0.1)
car1 = Car(0)
car1.fill(5)  # залили 5 литров
car1.ride(70)  # едем 70 км (если хватит топлива)

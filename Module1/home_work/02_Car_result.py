class Car:
    def __init__(self, capacity, gas_per_km):
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        # считаем, что новая машина всегда с пустым баком и без пробега:
        self.gas = 0
        self.mileage_km = 0

    def fill(self, liters):
        if liters < 0:
            print("Сливать бензин нельзя")
            return None
        gas = self.gas + liters
        if gas <= self.capacity:
            self.gas = gas
        else:
            self.gas = self.capacity
            extra_liters = gas - self.capacity
            print(f"Лишние литры: {extra_liters:.2f}")

    def ride(self, km):
        if km < 0:
            print("Скручивать счетчик нельзя")
            return None
        required_gas = self.gas_per_km * km  # сколько литров потребуется, чтобы проехать заданное расстояние
        if required_gas > self.gas:
            km = self.gas / self.gas_per_km
            self.gas = 0
        else:
            self.gas -= required_gas
        self.mileage_km += km
        print(f"Проехали {km:.2f} км")


if __name__ == "__main__":
    octavia = Car(45, 0.06)
    octavia.ride(10)
    octavia.fill(10)
    octavia.fill(40)
    octavia.ride(10)
    print(f'Пробег: {octavia.mileage_km}')
    octavia.ride(1000)
    print(f'Пробег: {octavia.mileage_km}')
    octavia.fill(-1)
    octavia.ride(-1)

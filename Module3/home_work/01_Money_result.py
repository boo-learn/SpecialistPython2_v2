class Money:
    def __init__(self, rub, penny):
        self.rub = rub
        self.penny = penny

    def __add__(self, other: 'Money'):
        penny = (self.rub * 100 + self.penny) + (other.rub * 100 + other.penny)
        rub = penny // 100
        penny = penny % 100
        return Money(rub, penny)

    def __sub__(self, other: 'Money'):
        penny = (self.rub * 100 + self.penny) - (other.rub * 100 + other.penny)
        if penny < 0:
            print(f'Отказано в оперции, недостаточно средств')
            return None
        rub = penny // 100
        penny = penny % 100
        return Money(rub, penny)

    def __mul__(self, other: int):
        penny = (self.rub * 100 + self.penny) * other
        rub = penny // 100
        penny = penny % 100
        return Money(rub, penny)

    def __gt__(self, other: 'Money'):
        return (self.rub * 100 + self.penny) > (other.rub * 100 + other.penny)

    def __eq__(self, other: 'Money'):
        return (self.rub * 100 + self.penny) == (other.rub * 100 + other.penny)

    def __lt__(self, other: 'Money'):
        return (self.rub * 100 + self.penny) < (other.rub * 100 + other.penny)

    def __mod__(self, other: int):
        penny = round((self.rub * 100 + self.penny) * other / 100)
        rub = penny // 100
        penny = penny % 100
        return Money(rub, penny)

    def __str__(self):
        penny = (self.rub * 100 + self.penny)
        rub = penny // 100
        penny = penny % 100
        return f'{rub}руб {penny}коп'

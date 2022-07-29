class Money:
    
    def __init__(self, rubles, penny):
        self.rubles = rubles + penny // 100
        self.penny = penny % 100

    def __str__(self):
        return f'{str(self.rubles) + " руб"} {str(self.penny) + " коп"}'

    def __add__(self, other_money):
        return Money(self.rubles + other_money.rubles, self.penny + other_money.penny)

    def __sub__(self, other_money):
        return Money(self.rubles - other_money.rubles, self.penny - other_money.penny)

    def __mul__(self, other_int):
        return Money(self.rubles * other_int, self.penny * other_int)

    def __gt__(self, other_money):
        return self.rubles > other_money.rubles

    def __lt__(self, other_money):
        return self.rubles < other_money.rubles

    def __eq__(self, other_money):
        return self.rubles == other_money.rubles

    def __ne__(self, other_money):
        return self.rubles != other_money.rubles

    def __mod__(self, other_int):
        return Money(round(self.rubles * (other_int / 100)), round(self.penny * (other_int/100)) + self.rubles % 100)

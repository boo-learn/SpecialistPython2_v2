class Money:
    pass
    # TODO: your code here
class Money:
    def __init__(self, ruble, penny):
        self.ruble = ruble
        self.penny = 100 * ruble + penny

    def __str__(self):
        return f'{self.penny // 100}руб {self.penny % 100}коп'

    def __add__(self, other):
        return Money(0, self.penny + other.penny)

    def __sub__(self, other):
        return Money(0, self.penny - other.penny)

    def __mul__(self, mul):
        return Money(0, self.penny * mul)

    def __gt__(self, other):
        return self.penny > other.penny

    def __eq__(self, other):
        return self.penny == other.penny

    def percent(self, per):
        percent_summ = round(self.penny * per / 100)
        rub_sum = percent_summ // 100
        penny_sum = percent_summ % 100
        return f'{rub_sum}руб {penny_sum}коп'

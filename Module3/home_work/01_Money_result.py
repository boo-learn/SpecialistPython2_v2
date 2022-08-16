import math
class Money:
    def __init__(self, rub, cop):

        self.rub = rub
        self.cop = cop

    def __add__(self, other_money):
        a = self.rub + other_money.rub
        b = self.cop + other_money.cop

        return Money(a + math.floor(b / 100), b - math.floor(b / 100) * 100)

    def __sub__(self, other_money):
        a = self.rub - other_money.rub
        b = self.cop - other_money.cop

        return Money(a + math.floor(b / 100), b - math.floor(b / 100) * 100)

    def __mul__(self, num):
        a = self.rub * num
        b = self.cop * num

        return Money(a + math.floor(b / 100), b - math.floor(b / 100) * 100)

    def __str__(self):

        return f"{self.rub+math.floor(self.cop/100)} {self.cop-math.floor(self.cop/100)*100}"

    def __gt__(self, other):

        if self.rub * 100 + self.cop > other.rub * 100 + other.cop:
            return self > other

    def __eq__(self, other):

        return self.rub * 100 + self.cop == other.rub * 100 + other.cop

    def __lt__(self):

        return not self > other and not self == other

    def __mod__(self, proc):
        a = round(((self.cop + self.rub * 100) / 100) * proc)
        return Money(0, a)


m1 = Money(20, 220)
print(m1)
m2 = Money(20, 35)
print(m2)
m3 = m1 + m2
print(m3)
m4 = m2 * 3
print(m4)

money_sum1 = Money(20, 60)
# Находим 21% от суммы
percent_sum = money_sum1 % 21
print(percent_sum)  # 4руб 33коп

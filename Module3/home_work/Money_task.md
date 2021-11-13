class Money:
    def __init__(self, ruble, kopek):
        self.kopek = ruble * 100 + kopek
        self.ruble = 0

    def __add__(self, other):
        return Money(self.ruble, self.kopek + other.kopek)

    def __sub__(self, other):
        return Money(self.ruble, self.kopek - other.kopek)

    def __mul__(self, num):
        return Money(self.ruble, self.kopek * num)

    def __mod__(self, pers):
        return Money(self.ruble, self.kopek * pers / 100)

    def __gt__(self, other):
        return self.kopek > other.kopek

    def __lt__(self, other):
        return self.kopek < other.kopek

    def __eq__(self, other):
        return self.kopek == other.kopek

    def __repr__(self):
         return f" {round(self.kopek // 100)} руб. {round(self.kopek % 100)} коп."

n = 2
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
money_result = money_sum1 + money_sum2
money_result_sub = money_sum1 - money_sum2
money_result_mul = money_sum1 * n
percent_sum = money_sum1 % 21


print (money_sum1)
print (money_sum2)
print(f"сложение: {money_result}")
print(f"вычитание: {money_result_sub}")
print(f"умножение на {n} :{money_result_mul}")
print(f"21 %: {percent_sum}")
print(money_sum1 > money_sum2)
print(money_sum1 < money_sum2)
print(money_sum1 == money_sum2)

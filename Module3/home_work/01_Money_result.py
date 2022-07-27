class Money:
    def __init__(self, rub, kop):
        self.rub = rub  # Рублей
        self.kop = kop  # Копеек

    def __str__(self):
        return f"{self.rub + self.kop // 100}руб {self.kop % 100}коп"

    def __add__(self, second_val):
        return Money(self.rub + second_val.rub, self.kop + second_val.kop)

    def __sub__(self, second_val):
        return Money((self.rub * 100 + self.kop - second_val.rub * 100 - second_val.kop) // 100,
                     (self.rub * 100 + self.kop - second_val.rub * 100 - second_val.kop) % 100)

    def __mul__(self, second_val):
        return Money((self.rub * 100 + self.kop) * second_val // 100, (self.rub * 100 + self.kop) * second_val % 100)

    def __mod__(self, second_val):
        return Money((self.rub * 100 + self.kop) * second_val / 100 // 100,
                      round((self.rub * 100 + self.kop) * second_val / 100 % 100))


money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

print(money_sum1)

money_result = money_sum1 + money_sum2
print(money_result) 

money_result = money_sum1 - money_sum2
print(money_result)

money_result = money_sum2 - money_sum1
print(money_result)

money_result = money_sum1 * 2
print(money_result)

money_result = money_sum1 * 0.1
print(money_result)

money_result = money_sum1 % 21
print(money_result)

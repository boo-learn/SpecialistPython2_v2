class Money:

    def __init__(self, rub, cop):
        self.rub = rub  # рубли
        self.cop = cop  # копейки
        if self.cop > 100:
            self.rub = int(self.rub) + int(self.cop//100)
            self.cop = int(self.cop) % 100

    def __str__(self):
        return f"{self.rub}руб {self.cop}коп"

    def __add__(self, othermoney): #можно было и просто через копейки
        if self.cop + othermoney.cop > 100:
            self.rub = self.rub + othermoney.rub + (self.cop + othermoney.cop) // 100
            self.cop = (self.cop + othermoney.cop) % 100
        else:
            self.rub = self.rub + othermoney.rub
            self.cop = self.cop + othermoney.cop
        return Money(self.rub, self.cop)

    def __mod__(self, percent): #как здесь
        self.cop = ((self.rub * 100 + self.cop) /100 )* percent
        return print(Money(0,self.cop))


# money_sum1 = Money(20, 120)
# print (money_sum1)
# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

money_sum3 = Money(20, 60)
# Находим 21% от суммы
percent_sum = money_sum3 % 21

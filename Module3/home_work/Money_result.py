class Money:
    def __init__(self, rub, kopeiki):
        self.rub = rub
        self.kopeiki = kopeiki
        if self.kopeiki > 99:
            self.rub = self.rub + kopeiki // 100
            self.kopeiki = self.kopeiki % 100
    # TODO: your code here

    def __str__(self):
        return f'{self.rub}руб {self.kopeiki}коп'

    def __add__(self, other_money):
        kopeiki_sum = self.kopeiki + other_money.kopeiki
        return Money(self.rub + other_money.rub + (kopeiki_sum)//100, kopeiki_sum%100)


# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1) # 21руб 20коп
# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

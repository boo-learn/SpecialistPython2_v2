class Money:
    def __init__(self, rubles, pennies):
        self.rubles = rubles + pennies // 100
        self.pennies = pennies % 100
    
    def __str__(self):
        return f"{self.rubles}руб. {self.pennies}коп."

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.pennies + other.pennies)

    def __mod__(self, other):
        return Money(0, round((self.rubles * 100 + self.pennies) * other / 100))

# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
print(money_sum1) # 21руб 20коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп


money_sum1 = Money(20, 60)
# Находим 21% от суммы
percent_sum = money_sum1 % 21
print(percent_sum)  # 4руб 33коп

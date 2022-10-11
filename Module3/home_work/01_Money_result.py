import random
import urllib.request

class Money:
    def __init__(self, ruble, penny):
        self.ruble = ruble
        self.penny = penny
    def __str__(self):
        sum = self.ruble * 100 + self.penny
        rub = sum//100
        pen = sum - rub * 100
        return f'{rub:.0f}руб {pen:.0f}коп'
    def __add__(self, second):
        add_obj = Money(self.ruble + second.ruble, self.penny + second.penny)
        return  add_obj
    def __sub__(self, second):
        #second_obj = Money(second.ruble, second.penny)
        first_penny = self.ruble * 100 + self.penny
        second_penny = second.ruble * 100 + second.penny
        delta = first_penny - second_penny
        if delta >= 0:
            rub = delta//100
            pen = delta - rub * 100
            return Money(rub, pen)
        else:
            print("Первое меньше второго")
    def __mul__(self, mult: int):
        pennies = (self.ruble * 100 + self.penny) * mult
        return Money(pennies//100, pennies - (pennies//100) * 100)
    def __gt__(self, second):
        return (self.ruble * 100 + self.penny) > (second.ruble * 100 + second.penny)

    def __lt__(self, second):
        return (self.ruble * 100 + self.penny) < (second.ruble * 100 + second.penny)
    def __eq__(self, second):
        return (self.ruble * 100 + self.penny) == (second.ruble * 100 + second.penny)
    def __ne__(self, second):
        return not (self.ruble * 100 + self.penny) == (second.ruble * 100 + second.penny)
    def __mod__(self, per: int):
        pennies = (self.ruble * 100 + self.penny) * per/100
        return Money(pennies // 100, pennies - (pennies // 100) * 100)



# Создаем две денежные суммы
money_sum1 = Money(141, 46)
money_sum2 = Money(15, 43)

money_result = money_sum1 + money_sum2
print("Сумма : ", money_result)

sub_result = money_sum1 - money_sum2
print("Разность : ", sub_result)

mult_result = money_sum1 * 5
print("Умножение : ", mult_result)

print(money_sum1 > money_sum2)
print(money_sum1 < money_sum2)
print(money_sum1 == money_sum2)
print(money_sum1 != money_sum2)

# Находим 21% от суммы
percent = 21
percent_sum = money_sum1 % percent

print(f"Процент ({percent}%) от {money_sum1} : ", percent_sum)








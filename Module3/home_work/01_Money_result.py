import urllib.request
import json


class Money:

    def __init__(self, rubles, coins):
        self.rubles = rubles
        self.coins = coins

    def __str__(self):
        money_sum = self.rubles * 100 + self.coins
        return "{} руб. {} коп.".format(money_sum // 100, money_sum % 100)

    def __add__(self, other_money):
        self.sum = self.rubles * 100 + self.coins
        other_money.sum = other_money.rubles * 100 + other_money.coins
        add_sum = self.sum + other_money.sum
        return Money(add_sum // 100, add_sum % 100)

    def __sub__(self, other_money):
        self.sum = self.rubles * 100 + self.coins
        other_money.sum = other_money.rubles * 100 + other_money.coins
        sub_sum = self.sum - other_money.sum
        return Money(sub_sum // 100, sub_sum % 100)

    def __mul__(self, number):
        self.sum = self.rubles * 100 + self.coins
        mul_sum = self.sum * number
        return Money(mul_sum // 100, mul_sum % 100)

    def __eq__(self, other_money):
        self.sum = self.rubles * 100 + self.coins
        other_money.sum = other_money.rubles * 100 + other_money.coins
        return self.sum == other_money.sum

    def __gt__(self, other_money):
        self.sum = self.rubles * 100 + self.coins
        other_money.sum = other_money.rubles * 100 + other_money.coins
        return self.sum > other_money.sum

    def __mod__(self, number):
        self.sum = self.rubles * 100 + self.coins
        mod_sum = round(self.sum * number / 100)
        return Money(mod_sum // 100, mod_sum % 100)

    def convert_eur(self):
        self.sum = self.rubles * 100 + self.coins
        convert_sum_eur = round(self.sum / data_dict["Valute"]["EUR"]["Value"])
        return Money(convert_sum_eur // 100, convert_sum_eur % 100)

    def convert_usd(self):
        self.sum = self.rubles * 100 + self.coins
        convert_sum_usd = round(self.sum / data_dict["Valute"]["USD"]["Value"])
        return Money(convert_sum_usd // 100, convert_sum_usd % 100)


money_sum1 = Money(20, 60)
money_sum2 = Money(10, 120)
money_sum3 = Money(10, 45)
money_sum4 = Money(10, 45)

money_result_add = money_sum1 + money_sum2
money_result_sub = money_sum3 - money_sum4
money_result_mul = money_sum1 * 2

print('Первая сумма:', money_sum1)
print('Вторая сумма:', money_sum2)
print('Третья сумма:', money_sum3)
print('Четвертая сумма:', money_sum4)
print(f"Сложение {money_sum1} и {money_sum2}:", money_result_add)
print(f"Вычитание {money_sum3} и {money_sum4}:", money_result_sub)
print(f"Умножение {money_sum1} на 2:", money_result_mul)
print(f"Равны ли суммы {money_sum3} и {money_sum4}:", money_sum3 == money_sum4)
print(f"Больше ли {money_sum1} чем {money_sum2}:", money_sum1 > money_sum2)
print(f"50% от {money_sum2}:", money_sum2 % 50)
print(f"21% от {money_sum1}:", money_sum1 % 21)

data = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
data_dict = json.loads(data)

print(money_sum1.convert_eur())
print(money_sum2.convert_usd())

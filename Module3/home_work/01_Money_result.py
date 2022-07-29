# Частичное выполнение задачи - без конвертации валюты и нативности

import urllib.request
import json


class Money:

    def __init__(self, rubles, coins):
        self.rubles = rubles  # рубли
        self.coins = coins  # копейки

    def sum(self):
        if self.coins > 99:
            self.rubles = self.rubles + self.coins // 100
            self.coins = self.coins % 100
        return int(self.rubles), int(self.coins)

    def to_str(self):
        return f'{self.sum()[0]} руб. {self.sum()[1]} коп.'

    def addition(self, other_money):
        add_rubles = self.sum()[0] + other_money.sum()[0]
        add_coins = self.sum()[1] + other_money.sum()[1]
        if add_coins > 99:
            add_rubles = add_rubles + add_coins // 100
            add_coins = add_coins % 100
        return f'{add_rubles} руб. {add_coins} коп.'

    def subtraction(self, other_money):
        subtract_rubles = self.sum()[0] - other_money.sum()[0]
        subtract_coins = self.sum()[1] - other_money.sum()[1]
        return f'{subtract_rubles} руб. {subtract_coins} коп.'

    def multiplication_by_number(self, number):
        multiply_rubles = self.sum()[0] * number
        multiply_coins = self.sum()[1] * number
        if multiply_coins > 99:
            multiply_rubles = multiply_rubles + multiply_coins // 100
            multiply_coins = multiply_coins % 100
        return f'{multiply_rubles} руб. {multiply_coins} коп.'

    def equal(self, other_money):
        if self.sum()[0] == other_money.sum()[0] and self.sum()[1] == other_money.sum()[1]:
            return f'{self.to_str()} равны {other_money.to_str()}'
        return f'{self.to_str()} не равны {other_money.to_str()}'

    def comparison(self, other_money):
        if self.sum()[0] > other_money.sum()[0]:
            return f'{self.to_str()} больше {other_money.to_str()}'
        elif self.sum()[0] == other_money.sum()[0]:
            if self.sum()[1] > other_money.sum()[1]:
                return f'{self.to_str()} больше {other_money.to_str()}'
            return f'{self.to_str()} меньше {other_money.to_str()}'
        else:
            return f'{self.to_str()} меньше {other_money.to_str()}'

    def percent_of_sum(self, percent):
        summ = self.sum()[0] + self.sum()[1] / 100
        percent_sum = summ * percent / 100
        return f'{int(percent_sum)} руб. {int((percent_sum-int(percent_sum))*100)} коп.'


data = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
data_dict = json.loads(data)
print(data_dict)

money1 = Money(10, 99)
money2 = Money(20, 5)
print(f"Первая сумма {money1.to_str()}")
print(f"Вторая сумма {money2.to_str()}")

eq = money1.equal(money2)
print(f"Равны или не равны: {eq}")

comp = money1.comparison(money2)
print(f"Сравнение: {comp}")

add = money1.addition(money2)
print(f"Сложение: {add}")

sub = money1.subtraction(money2)
print(f"Вычитание: {sub}")

mult = money1.multiplication_by_number(2)
print(f"Умножение на число: {mult}")

pr = money1.percent_of_sum(10)
print(f"Процент от суммы: {pr}")

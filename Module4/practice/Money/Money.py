import urllib.request
import json


class Money:

    def __init__(self, rubles: int, kopeck: int):
        self.rubles = rubles
        self.kopeck = kopeck
    
    @staticmethod 
    def calc_total_sum(rub, kop):
        return rub * 100 + kop
    
    def __str__(self):
        if self.kopeck >= 100:
            self.rubles += self.kopeck // 100
        return f'{self.rubles}руб {self.kopeck % 100}коп'

    def __add__(self, other_money):
        new_money_sum = Money(self.rubles + other_money.rubles, self.kopeck + other_money.kopeck)
        return new_money_sum

    def __sub__(self, other_money):
        sum = self.calc_total_sum(self.rubles, self.kopeck) - self.calc_total_sum(other_money.rubles, other_money.kopeck)
        rub = sum // 100
        kop = sum % 100
        return Money(rub if rub >= 0 else 0, kop if rub >= 0 else 0)

    def __mod__(self, percent):
        sum = (self.calc_total_sum(self.rubles, self.kopeck)) * percent / 100
        rubles = int(sum // 100)
        kopeck = round(sum % 100)
        return Money(rubles, kopeck)

    def __gt__(self, other_money):
        return self.calc_total_sum(self.rubles, self.kopeck) > self.calc_total_sum(other_money.rubles, other_money.kopeck)

    def __lt__(self, other_money):
        return self.calc_total_sum(self.rubles, self.kopeck) < self.calc_total_sum(other_money.rubles, other_money.kopeck)

    def __eq__(self, other_money):
        return self.calc_total_sum(self.rubles, self.kopeck) == self.calc_total_sum(other_money.rubles, other_money.kopeck)

    def __ne__(self, other_money):
        return self.calc_total_sum(self.rubles, self.kopeck) != self.calc_total_sum(other_money.rubles, other_money.kopeck)

    def convert(self):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        currency = data_dict['Valute']
        print()
        sum = (self.rubles + self.kopeck) / 100
        return print(
            f'{self.rubles}руб {self.kopeck % 100}коп-это: \n{round(sum * currency["USD"]["Value"], 2)} долларов,\n{round(sum * currency["EUR"]["Value"], 2)} евро')


money_sum1 = Money(20, 280)
print(money_sum1)

money_sum1 = Money(20, 120)
money_sum2 = Money(10, 10)
money_result = money_sum1 + money_sum2
print(money_result)

money_sum1 = Money(20, 15)

money_sum2 = Money(21, 20)
money_result = money_sum1 - money_sum2
print(money_result)

money_sum1 = Money(20, 60)
money_sum3 = Money(20, 60)
# Находим 21% от суммы
percent_sum = money_sum1 % 21

print(percent_sum)  # 4руб 33коп

money_sum1.convert()

print(money_sum2 > money_sum1)
print(money_sum1 != money_sum2)

import json
import urllib.request


class Money:
    DATA = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
    DATA_DICT = json.loads(DATA)

    def __init__(self, rub, kop):
        self.rubles = rub
        self.kopecks = kop

    def __add__(self, other_sum):
        result = self.rubles + other_sum.rubles + (self.kopecks + other_sum.kopecks) / 100
        return f"{round(result * 100 // 100)} руб. {round(result * 100 % 100)} коп."

    def __sub__(self, other_sum):
        result = self.rubles + self.kopecks / 100 - other_sum.rubles - other_sum.kopecks / 100
        return f"{round(result * 100 // 100)} руб. {round(result * 100 % 100)} коп."

    def __mul__(self, int_num):
        result = (self.rubles + self.kopecks / 100) * int_num
        return f"{round(result * 100 // 100)} руб. {round(result * 100 % 100)} коп."

    def __gt__(self, other_sum):
        return self.rubles + self.kopecks / 100 > other_sum.rubles + other_sum.kopecks / 100

    def __eq__(self, other_sum):
        return self.rubles + self.kopecks / 100 == other_sum.rubles + other_sum.kopecks / 100

    def __lt__(self, other_sum):
        return self.rubles + self.kopecks / 100 < other_sum.rubles + other_sum.kopecks / 100

    def __ne__(self, other_sum):
        return self.rubles + self.kopecks / 100 != other_sum.rubles + other_sum.kopecks / 100

    def __mod__(self, int_num):
        result = (self.rubles + self.kopecks / 100) * int_num * 0.01
        return f"{round(result * 100 // 100)} руб. {round(result * 100 % 100)} коп."

    def convert(self, Valute):
        if Valute == 'USD':
            result = round((self.rubles + self.kopecks / 100) / self.DATA_DICT['Valute']['USD']['Value'], 2)
            return f"{round(result * 100 // 100)} $ {round(result * 100 % 100)} ₵"
        elif Valute == 'EUR':
            result = round((self.rubles + self.kopecks / 100) / self.DATA_DICT['Valute']['EUR']['Value'], 2)
            return f"{round(result * 100 // 100)} € {round(result * 100 % 100)} ₵"

money1 = Money(175, 10)
money2 = Money(20, 60)
print(money1.__add__(money2))
print(money1.__sub__(money2))
print(money1.__mul__(5))
print(money1.__lt__(money2))
print(money1.__gt__(money2))
print(money1.__eq__(money2))
print(money1.__ne__(money2))

percent_sum = money1 % 21
print(percent_sum)

print(money1.convert('USD'))
print(money1.convert('EUR'))

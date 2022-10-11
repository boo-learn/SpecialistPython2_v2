import urllib.request
import json


class Money:
    def __init__(self, rub, kop):
        total_kop = rub * 100 + kop
        if total_kop > 0:
            self.rub = total_kop // 100
            self.kop = total_kop % 100
        else:
            self.rub = 0
            self.kop = 0

    def __str__(self):
        return f'{self.rub}руб {self.kop}коп'

    def __add__(self, other):
        rub = self.rub + other.rub
        kop = self.kop + other.kop
        return Money(rub, kop)

    def __sub__(self, other):
        rub = self.rub - other.rub
        kop = self.kop - other.kop
        return Money(rub, kop)

    def __mul__(self, other):
        rub = self.rub * other
        kop = self.kop * other
        return Money(rub, kop)

    def __eq__(self, other):
        self_kop = self.rub * 100 + self.kop
        other_kop = other.rub * 100 + other.kop
        return self_kop == other_kop

    def __gt__(self, other):
        self_kop = self.rub * 100 + self.kop
        other_kop = other.rub * 100 + other.kop
        return self_kop > other_kop

    def __lt__(self, other):
        self_kop = self.rub * 100 + self.kop
        other_kop = other.rub * 100 + other.kop
        return self_kop < other_kop

    def __mod__(self, other):
        self_kop = self.rub * 100 + self.kop
        total_kop = round(self_kop * other / 100)
        return Money(0, total_kop)

    def convert(self, currency):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        value = data_dict['Valute'][currency]['Value']
        self_kop = self.rub * 100 + self.kop
        return self_kop / value / 100


# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

print("sum1 = ", money_sum1)
print("sum2 = ", money_sum2)
print("sum1 + sum2 = ", money_sum1 + money_sum2)
print("sum1 - sum2 = ", money_sum1 - money_sum2)
print("sum1 = sum2 = ", money_sum1 == money_sum2)
print("sum1 > sum2 = ", money_sum1 > money_sum2)
print("sum1 < sum2 = ", money_sum1 < money_sum2)
print("sum1 % 21 = ", money_sum1 % 21)
print("sum1.convert('EUR') = ", money_sum1.convert('EUR'))
print("sum1.convert('USD') = ", money_sum1.convert('USD'))

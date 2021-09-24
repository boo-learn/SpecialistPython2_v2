import urllib.request
import json

class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def to_str(self):
        return f"{self.rub} руб {self.kop} коп"

    def __str__(self):
        return f"{self.rub} руб {self.kop} коп"

    def plus(self, other_sum):
        return f"{self.rub + other_sum.rub} руб {self.kop + other_sum.kop} kop"

    def minus(self, other_sum):
        return f"{self.rub - other_sum.rub} руб {self.kop - other_sum.kop} kop"

    def multiply(self, num):
        return f"{self.rub * num} руб {self.kop * num} коп"

    def __gt__(self, other_sum):
        if self.rub == other_sum.rub:
            return self.kop > other_sum.kop
        else:
            return self.rub > other_sum.rub

    def __lt__(self, other_sum):
        if self.rub == other_sum.rub:
            return self.kop < other_sum.kop
        else:
            return self.rub < other_sum.rub

    def __ge__(self, other_sum):
        if self.rub == other_sum.rub:
            return self.kop >= other_sum.kop
        else:
            return self.rub >= other_sum.rub

    def __le__(self, other_sum):
        if self.rub == other_sum.rub:
            return self.kop <= other_sum.kop
        else:
            return self.rub <= other_sum.rub

    def __eq__(self, other_sum):
        if self.rub == other_sum.rub:
            return self.kop == other_sum.kop
        else:
            return self.rub == other_sum.rub

    def __ne__(self, other_sum):
        if self.rub == other_sum.rub:
            return self.kop != other_sum.kop
        else:
            return self.rub != other_sum.rub

    def sum_percent(self, percent):
        return f"{percent}% от суммы: {round(self.rub * percent/100)} руб {round(self.kop * percent/100)} коп"

    def convert(self, currency):
        url = f'https://www.cbr-xml-daily.ru/daily_json.js'
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        curr_rate = data_dict['Valute'][currency]['Value']
        return f"Сумма в {currency}: {(self.rub + (self.kop/100))/ curr_rate}"


sum_money1 = Money(3000, 65)
sum_money2 = Money(1450, 14)
print(sum_money1)
print(sum_money2)
print(sum_money1.plus(sum_money2))
print(sum_money1.minus(sum_money2))
print(sum_money2.multiply(5))
print(sum_money1 > sum_money2)
print(sum_money1.sum_percent(10))
print(sum_money1.convert("USD"))
print(sum_money2.convert("EUR"))
print(sum_money1.convert("GBP"))
print(sum_money1.convert("AUD"))



import json
import urllib.request


class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop
        if kop > 100:
            self.rub += kop // 100
            self.kop = kop % 100

    def __str__(self):
        return f"{self.rub} руб. {self.kop} коп."

    def __add__(self, other_money):
        return Money(self.rub + other_money.rub, self.kop + other_money.kop)

    def __sub__(self, other_money):
        return Money(self.rub - other_money.rub, self.kop - other_money.kop)    

    def __mul__(self, some_integer):
        return Money(self.rub * some_integer, self.kop * some_integer)   

    def __lt__(self, other_money):
        return Money(self.rub < other_money.rub, self.kop < other_money.kop)

    def __le__(self, other_money):
        return Money(self.rub <= other_money.rub, self.kop <= other_money.kop)

    def __gt__(self, other_money):
        return Money(self.rub > other_money.rub, self.kop > other_money.kop)

    def __ge__(self, other_money):
        return Money(self.rub >= other_money.rub, self.kop >= other_money.kop)

    def per_cent(self, percent):
        return Money(round((self.rub * percent) / 100), round((self.kop * percent) / 100))

    def convert(self):
        choose_the_currency = str(input("Выберите валюту (USD или EUR): "))
        data = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
        data_dict = json.loads(data)
        valutes = {}
        valute = {}
        rate = 0
        for key, value in data_dict.items():
            if key == "Valute":
                valutes.update(value)
                for key, value in valutes.items():
                    if key == choose_the_currency:
                        valute.update(value)
                        for key, value in valute.items():
                            if key == "Value":
                                rate = value
        return f"{round(self.rub /rate)},{round(self.kop / rate)} {choose_the_currency}."
        


money1 = Money(12, 345)
money2 = Money(4, 112)
money3 = money1 + money2
money4 = money1 - money2
money5 = money1 * 15
money6 = money1 < money2
money7 = money1 <= money2
money8 = money1 > money2
money9 = money1 >= money2
money10 = Money(30, 122)
percent_sum = money10.per_cent(10)
money11 = Money(1556, 74)
money12 = money11.convert()

print(money1)
print(money2)
print(money3)
print(money4)
print(money6)
print(money7)
print(money8)
print(money9)
print(percent_sum)
print(money12)

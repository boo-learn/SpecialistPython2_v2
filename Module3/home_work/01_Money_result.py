import urllib.request
import json

class Money:
# по хорошему надо сюда тогда добавить и код валюты,но это уже нет времени и сил
    def __init__(self, rub, kop):
        self.convert(rub, kop)
        #self.rub = rub + (kop // 100)
        #self.kop = kop % 100

    def convert(self, rub, kop):
        self.rub = rub + int(kop / 100)
        self.kop = kop % 100

    def sum_kop(self, item):
        return item.rub*100 + item.kop

    def __add__(self, other):
        return Money(0, self.sum_kop(self) + self.sum_kop(other))

    def __sub__(self, other):
        return Money(0, self.sum_kop(self) - self.sum_kop(other))

    def __mul__ (self, n):
        return Money(0, self.sum_kop(self) * n)

    def __eq__(self, other):
        return self.sum_kop(self) == self.sum_kop(other)

    def __ne__(self, other):
        return self.sum_kop(self) != self.sum_kop(other)

    def __gt__(self, other):
        return self.sum_kop(self) > self.sum_kop(other)

    def __lt__(self, other):
        return self.sum_kop(self) < self.sum_kop(other)

    def __mod__(self, proc):
        return Money(0, int((self.sum_kop(self) * proc) / 100))

    def convert_currency(self, curr):
        data = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
        data_dict = json.loads(data)
        rate = data_dict["Valute"][curr]["Value"]
#        usd_rate = data_dict["Valute"]["USD"]["Value"]
 #       eur_rate = data_dict["Valute"]["EUR"]["Value"]
        return Money(0, int((self.sum_kop(self) / rate)))

m1 = Money(10,250)
m2 = Money(15,350)

m3 = m1 + m2
m4 = m1 - m3
m5 = m2 * 3
m6 = m5%30

m7 = m3.convert_currency("USD")

print(f"m1: {m1.rub}, {m1.kop}")
print(f"m2: {m2.rub}, {m2.kop}")
print(f"m3: {m3.rub}, {m3.kop}")
print(f"m4: {m4.rub}, {m4.kop}")
print(f"m5: {m5.rub}, {m5.kop}")
print(f"m1==m1: {m1 == m1}")
print(f"m1!=m2: {m1 != m2}")
print(f"m1 > m2: {m1 > m2}")
print(f"m1 < m2: {m1 < m2}")
print(f"m6: {m6.rub}, {m6.kop}")
print(f"m7: {m7.rub}, {m7.kop}")


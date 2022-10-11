import urllib.request
import json

class Money:
    pass
    def __init__(self, rubles, kopeks):
        self.rubles = rubles  # Рубли
        self.kopeks = kopeks  # Копейки

    def __repr__(self):
        return f"{self.rubles + self.kopeks // 100}руб {self.kopeks % 100}коп"

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.kopeks + other.kopeks)

    def __sub__(self, other):
        return Money(self.rubles - other.rubles, self.kopeks - other.kopeks)

    def __mul__(self, other: int):
        return Money(self.rubles * other, self.kopeks * other)

    def __gt__(self, other):
        return (self.rubles * 100 + self.kopeks) > (other.rubles * 100 + other.kopeks)

    def __lt__(self, other):
        return (self.rubles * 100 + self.kopeks) < (other.rubles * 100 + other.kopeks)

    def __eq__(self, other):
        return (self.rubles * 100 + self.kopeks) == (other.rubles * 100 + other.kopeks)

    def __ne__(self, other):
        return (self.rubles * 100 + self.kopeks) != (other.rubles * 100 + other.kopeks)

    def __mod__(self, other: int):
        return Money(round((self.rubles * 100 + self.kopeks) * other / 100 // 100), round((self.rubles * 100 + self.kopeks) * other / 100 % 100))

    def convert(self, currency):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        return round((self.rubles * 100 + self.kopeks) / 100 / data_dict["Valute"][currency]["Value"],2)


# print("USD:", money_sum1.convert("USD"))
# print("EUR:", money_sum1.convert("EUR"))

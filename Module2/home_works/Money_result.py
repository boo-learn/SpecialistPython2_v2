import json
import urllib.request


class Money:
    def __init__(self, rub, cop):
        self.common_cost = rub * 100 + cop

    def __str__(self):
        return f'{int(self.common_cost // 100)} руб {int(self.common_cost % 100)} коп'

    def __add__(self, other):
        return Money((self.common_cost + other.common_cost) // 100, (self.common_cost + other.common_cost) % 100)

    def __sub__(self, other):
        return Money((self.common_cost - other.common_cost) // 100, (self.common_cost - other.common_cost) % 100)

    def __mul__(self, other):
        return Money((self.common_cost * other) // 100, (self.common_cost * other) % 100)

    def __lt__(self, other):
        return self.common_cost < other.common_cost

    def __le__(self, other):
        return self.common_cost <= other.common_cost

    def __gt__(self, other):
        return self.common_cost > other.common_cost

    def __ge__(self, other):
        return self.common_cost >= other.common_cost

    def __ne__(self, other):
        return self.common_cost != other.common_cost

    def __eq__(self, other):
        return self.common_cost == other.common_cost

    def __mod__(self, other):
        return Money((self.common_cost * other / 100) // 100, (self.common_cost * other / 100) % 100)

    def convert(self, valute: str):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        usd_currency = Money(round(data_dict['Valute']['USD']['Value']),
                             round(data_dict['Valute']['USD']['Value'], 2) % 1 * 100)
        eur_currency = Money(round(data_dict['Valute']['EUR']['Value']),
                             round(data_dict['Valute']['EUR']['Value'], 2) % 1 * 100)
        if valute == "USD":
            usd_cost = self.common_cost / usd_currency.common_cost
            print(f'{int(usd_cost // 1)} долларов {int((usd_cost % 1) * 100)} центов')
        elif valute == "EUR":
            eur_cost = self.common_cost / eur_currency.common_cost
            print(f'{int(eur_cost // 1)} евро {int((eur_cost % 1) * 100)} евроцентов')
        else:
            print('Введите валюту правильно - "USD" или "EUR"')



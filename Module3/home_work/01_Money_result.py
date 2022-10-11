import urllib.request
import json

class Money:
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    def __init__(self, rubles, pennies):
        self.rubles = rubles
        self.pennies = pennies

    def __str__(self):
        if self.pennies // 100 >= 1:
            self.rubles = self.rubles + self.pennies//100
            self.pennies = self.pennies%100
        return f"{self.rubles}руб {self.pennies}коп"

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.pennies + other.pennies)

    def __sub__(self, other):
        return Money(self.rubles - other.rubles, self.pennies - other.pennies)

    def __mul__(self, x):
        return Money(self.rubles * x, self.pennies * x)

    def multiplication(self, other):
        return Money(self.rubles + other.rubles, self.pennies + other.pennies)

    def __lt__(self, other):
        return (self.rubles + self.pennies) < (other.rubles + other.pennies)

    def convert(self):
        data = urllib.request.urlopen(Money.url).read()
        data_dict = json.loads(data)
        dollar_exchange_rate = data_dict['Valute']['USD']["Value"]
        euro_exchange_rate = data_dict['Valute']['EUR']["Value"]
        exchange_value = (self.rubles + self.pennies)
        return f"Сумма в долларах составляет: {round(exchange_value/dollar_exchange_rate, 3)}, сумма в евро составляет: {round(exchange_value/euro_exchange_rate, 3)}"

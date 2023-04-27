import json
import urllib.request


class Money:
    def __init__(self, notes: int, coins: int):
        self.total_in_coins = notes * 100 + coins
        self.coins = int(self.total_in_coins % 100)
        self.notes = int((self.total_in_coins - self.coins) / 100)

        if self.coins >= 100 and self.total_in_coins >= 0:
            self.notes += self.coins // 100
            self.coins = self.coins % 100

        if self.coins <= 100 and self.total_in_coins < 0:
            if self.coins != 0:
                self.coins = (100 - self.coins % 100)*-1
            else:
                self.coins = 0
            self.notes = int((self.total_in_coins - self.coins) / 100)

    def __str__(self):
        if self.total_in_coins > 0:
            return f"{self.notes}руб {abs(self.coins)}коп"
        elif self.total_in_coins < 0:
            return f"{self.notes}руб {abs(self.coins)}коп"
        elif self.total_in_coins == 0:
            return f"0руб 0коп"

    def __add__(self, other):
        return Money(self.notes + other.notes, self.coins + other.coins)

    def __sub__(self, other):
        return Money(self.notes - other.notes, self.coins - other.coins)

    def __mul__(self, other):

        return Money(self.notes * other, self.coins * other)

    def __gt__(self, other):
        return self.total_in_coins > other.total_in_coins

    def __lt__(self, other):
        return self.total_in_coins < other.total_in_coins

    def __eq__(self, other):
        return self.total_in_coins == other.total_in_coins

    def __ne__(self, other):
        return self.total_in_coins != other.total_in_coins

    def __mod__(self, other):
        percent = round((self.total_in_coins/10000)*other, 2)
        return Money(percent, 0)

    def convert(self, currency: str):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        currency_rate = data_dict["Valute"][f'{currency.upper()}']['Value']
        exchanged = round(self.total_in_coins / currency_rate/ 100, 2)
        return f"{exchanged}({currency.upper()}) за {self.notes}руб. {abs(self.coins)}коп."

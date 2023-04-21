import json
import urllib.request


class Money:
    def __init__(self, notes: int, coins: int):
        self.notes = notes
        self.coins = coins
        if self.coins >= 100:
            self.notes += self.coins // 100
            self.coins = self.coins % 100

        if self.coins > 0 and self.notes > 0:  # Если вернем отрицательное число то "-" перед рулями
            self.float_sum = float(f"{self.notes}.{self.coins}")
        else:
            self.float_sum = float(f"-{abs(self.notes)}.{abs(self.coins)}")
            print(self.float_sum)

    def __str__(self):
        return f"{self.notes} руб. {self.coins} коп."

    def __add__(self, other):
        return Money(self.notes + other.notes, self.coins + other.coins)

    def __sub__(self, other):
        a = self.notes - other.notes
        b = self.coins - other.coins
        if a > 0 and b > 0:  # Если вернем отрицательное число то - перед рулями
            return Money(self.notes - other.notes, self.coins - other.coins)
        else:
            return Money(self.notes - other.notes, abs(self.coins - other.coins))

    def __mul__(self, other):
        return Money(self.notes * other.notes, self.coins * other.coins)

    def __gt__(self, other):
        return self.float_sum > other.float_sum

    def __lt__(self, other):
        return self.float_sum < other.float_sum

    def __eq__(self, other):
        return self.float_sum == other.float_sum

    def __ne__(self, other):
        return self.float_sum != other.float_sum

    def __mod__(self, other):
        sum_percent = round((self.float_sum/100*other), 2)
        lst_percent = str(sum_percent).split(".")
        return Money(int(lst_percent[0]), int(lst_percent[1]))

    def convert(self, currency: str):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        currency_rate = data_dict["Valute"][f'{currency.upper()}']['Value']
        exchanged = round(self.float_sum / currency_rate, 2)
        return f"{exchanged}-{currency.upper()}- за {self.notes}руб. {self.coins}коп."

# money1 = Money(-19, 120)
# money2 = Money(20, 130)
# print(money1, money2)
# print(money1 + money2)
# print(money1 - money2)
# if money1 > money2:
#     print(f"{money1} больше {money2}")
# if money1 < money2:
#     print(f"{money1} меньше {money2}")
# if money1 == money2:
#     print(f"{money1} равно {money2}")
# if money1 != money2:
#     print(f"{money1} не равно {money2}")
# print(money1 % 10)
# print(money1.convert('usd'))

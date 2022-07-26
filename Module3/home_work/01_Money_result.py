import urllib.request
import json


class Money:

    def __init__(self, rubl, kop, currency="RUB"):
        self.amount = rubl + (kop / 100)
        self.currency = currency

    def __str__(self):
        if self.currency == "RUB":
            return f"{int(self.amount)} руб {abs(round((self.amount - int(self.amount)) * 100))} коп"
        if self.currency == "USD":
            return f"{int(self.amount)} дол {abs(round((self.amount - int(self.amount)) * 100))} цент"
        if self.currency == "EUR":
            return f"{int(self.amount)} евро {abs(round((self.amount - int(self.amount)) * 100))} цент"

    def __add__(self, other_money):
        amount = self.amount + other_money.amount
        return Money(int(amount), round((amount - int(amount)) * 100))

    def __sub__(self, other_money):
        amount = self.amount - other_money.amount
        return Money(int(amount), round((amount - int(amount)) * 100))

    def __mul__(self, cnt):
        amount = self.amount * cnt
        return Money(int(amount), round((amount - int(amount)) * 100))

    def __eq__(self, other_money):
        return self.amount == other_money.amount

    def __lt__(self, other_money):
        return self.amount < other_money.amount

    def __gt__(self, other_money):
        return self.amount > other_money.amount

    def __ne__(self, other_money):
        return self.amount != other_money.amount

    def __mod__(self, percent):
        amount = round(self.amount * percent / 100, 2)
        return Money(int(amount), round((amount - int(amount)) * 100))

    def convert(self, currency):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)['Valute']
        if currency in data_dict:
            current_currency = data_dict[currency]
            amount = self.amount / (current_currency['Value'] / current_currency['Nominal'])
        return Money(int(amount), round((amount - int(amount)) * 100), currency)


money_sum1 = Money(20, 120)

print(money_sum1)  # 21руб 20коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

money_result = money_sum2 - money_sum1
print(money_result)

money_result = money_sum1 * 3
print(money_result)

if money_sum1 < money_sum2:
    print('lt', money_sum1 < money_sum2)

if money_sum1 > money_sum2:
    print('gt', money_sum1 > money_sum2)

if money_sum1 == money_sum2:
    print('eq', money_sum1 == money_sum2)

if money_sum1 != money_sum2:
    print('ne', money_sum1 != money_sum2)

# Находим 21% от суммы
percent_sum = money_sum1 % 21

print(percent_sum)  # 4руб 33коп

money_sum1_usd = money_result.convert('USD')
print(money_result, money_sum1_usd)
money_sum1_eur = money_result.convert('EUR')
print(money_result, money_sum1_eur)


import urllib.request
import json


class Money:
    def __init__(self, ruble, kopeck):
        self.ruble = ruble
        self.kopeck = kopeck

    def __str__(self):
        if self.kopeck >= 100 or self.kopeck < 0:
            self.ruble += self.kopeck // 100
            self.kopeck = self.kopeck % 100
        return f"{self.ruble} руб. {self.kopeck} коп."

    def change_type(self, currency_type: str): # используется внутри функции convert
        self.currency_type = currency_type
        if currency_type.upper() == "USD":
            return f"{self.ruble} долларов {self.kopeck} центов."
        elif currency_type.upper() == "EUR":
            return f"{self.ruble} евро {self.kopeck} центов."
        else:
            return f"{self.ruble}.{self.kopeck}."

    def __add__(self, money_term):
        return Money(self.ruble + money_term.ruble, self.kopeck + money_term.kopeck)

    def __sub__(self, money_subtrahend):
        return Money(self.ruble - money_subtrahend.ruble, self.kopeck - money_subtrahend.kopeck)

    def __mul__(self, factor):
        return Money(round(self.ruble * factor), round(self.kopeck * factor))

    def __gt__(self, money_compassion):
        return self.ruble > money_compassion.ruble or (
                self.ruble == money_compassion.ruble and self.kopeck > money_compassion.kopeck)

    def __lt__(self, money_compassion):
        return self.ruble < money_compassion.ruble or (
                self.ruble == money_compassion.ruble and self.kopeck < money_compassion.kopeck)

    def __eq__(self, money_compassion):
        return self.ruble == money_compassion.ruble and self.kopeck == money_compassion.kopeck

    def compassion(self, money_compassion): # сравнение двух значений строкой
        if self.ruble > money_compassion.ruble or (
                self.ruble == money_compassion.ruble and self.kopeck > money_compassion.kopeck):
            return f"{self} больше, чем {money_compassion}"
        elif self.ruble == money_compassion.ruble and self.kopeck == money_compassion.kopeck:
            return f"{self} суммы равны"
        else:
            return f"{self} меньше, чем {money_compassion}"

    def percent(self, percent): # вычисление процента при одном значении. Процент высчитывается после перевода всей суммы в копейки (*100)
        a = round(((self.ruble * 100 + self.kopeck) / 100) * percent)
        return Money(a // 100, a % 100)

    def percent_sum(self, money_term, percent: int):
        a = round(((self.ruble * 100 + self.kopeck + money_term.ruble * 100 + money_term.kopeck) / 100) * percent)
        return Money(a // 100, a % 100)

    def convert(self, currency_type): # используется функция change_type
        currency_type = currency_type.upper()
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        converting = Money(round(self.ruble / data_dict["Valute"][currency_type]["Value"]),
                           round(self.kopeck / data_dict["Valute"][currency_type]["Value"]))
        return converting.change_type(currency_type)

# Обновлённая версия
# 2023-04-23

import urllib.request
import json

URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def str_from_total_kops(total_kops: int) -> str:
    if total_kops >= 0:
        return f"{total_kops // 100} руб. {total_kops % 100:02} коп."
    else:
        return f"-{-total_kops // 100} руб. {-total_kops % 100:02} коп."


class Money:
    def __init__(self, rubs: int = 0, kops: int = 0):
        if rubs >= 0:
            self.__total = rubs * 100 + kops
        else:
            self.__total = rubs * 100 - kops

    def __str__(self) -> str:
        return str_from_total_kops(self.get_total())

    def __add__(self, other_money) -> str:
        return str_from_total_kops(self.get_total() + other_money.get_total())

    def __sub__(self, other_money) -> str:
        return str_from_total_kops(self.get_total() - other_money.get_total())

    def __mul__(self, k) -> str:
        return str_from_total_kops(self.get_total() * k)

    def __gt__(self, other_money) -> bool:
        return self.get_total() > other_money.get_total()

    def __lt__(self, other_money) -> bool:
        return self.get_total() < other_money.get_total()

    def __eq__(self, other_money) -> bool:
        return self.get_total() == other_money.get_total()

    def __ne__(self, other_money) -> bool:
        return self.get_total() != other_money.get_total()

    def __mod__(self, percent):
        return str_from_total_kops(round(self.get_total() / 100 * percent))

    def get_total(self):
        return self.__total

    def convert(self, currency="USD"):
        __data = urllib.request.urlopen(URL).read()
        __data_dict = json.loads(__data)
        if currency == "USD":
            __exchange_rate = __data_dict["Valute"]["USD"]["Value"]
        elif currency == "EUR":
            __exchange_rate = __data_dict["Valute"]["EUR"]["Value"]
        else:
            # В случае неправильно указанной валюты возвращаем значение по курсу 1:1
            __exchange_rate = 1
        __total_rubs = self.get_total() // 100 + self.get_total() % 100 / 100
        return round(__total_rubs / __exchange_rate, 2)


money1 = Money(10, 46)
money2 = Money(10, 48)

print(f"Даны две суммы: {money1} и {money2}")
print(f"Проверка суммы: {money1} + {money2} = {money1 + money2}")
print(f"Проверка разности: {money1} - {money2} = {money1 - money2}")
print(f"Проверка умножения: {money1} * 3 = {money1 * 3}")
print("Сравнение сумм: ", end="")
print(f"Больше ли {money1}, чем {money2}? - {money1 > money2}")
print("Сравнение равенства сумм: ", end="")
if money1 == money2:
    print(f"{money1} равны {money2}")
else:
    print(f"{money1} не равны {money2}")
print("Сравнение неравенства сумм: ", end="")
if money1 != money2:
    print(f"{money1} не равны {money2}")
else:
    print(f"{money1} равны {money2}")
print(f"Проверка процента от суммы: {money1} % 20 = {money1 % 20}")
print(f"Проверка перевода суммы в доллары: {money1} составляют {money1.convert()} долларов США")
conv_eur = money1.convert("EUR")
print(f"Проверка перевода суммы в евро: {money1} составляют {conv_eur} евро")

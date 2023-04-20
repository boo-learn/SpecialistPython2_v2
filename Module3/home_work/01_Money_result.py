# Алексей Ерёмин, Москва
# 2023-04-21

import urllib.request
import json

URL = "https://www.cbr-xml-daily.ru/daily_json.js"


class Money:
    def __init__(self, rub: int, kop: int):
        self.rub = rub
        self.kop = kop
        if kop >= 100:
            self.rub += self.kop // 100
            self.kop = kop % 100

    def __str__(self):
        return f"{self.rub} руб. {self.kop:02} коп."

    def __add__(self, money2) -> str:
        total = self.rub * 100 + self.kop + money2.rub * 100 + money2.kop
        total_rub = total // 100
        total_kop = total % 100
        return f"{total_rub} руб. {total_kop:02} коп."

    def __sub__(self, money2):
        total = (self.rub * 100 + self.kop) - (money2.rub * 100 + money2.kop)
        if total >= 0:
            total_rub = total // 100
            total_kop = total % 100
        else:
            total_rub = -1 * (-total // 100)
            total_kop = -total % 100
        return f"{total_rub} руб. {total_kop:02} коп."

    def __mul__(self, k):
        total = (self.rub * 100 + self.kop) * k
        total_rub = total // 100
        total_kop = total % 100
        return f"{total_rub} руб. {total_kop:02} коп."

    def __gt__(self, money2):
        total_kops_1 = self.rub * 100 + self.kop
        total_kops_2 = money2.rub * 100 + money2.kop
        return total_kops_1 > total_kops_2

    def __lt__(self, money2):
        return not self.__gt__(money2)

    def __eq__(self, money2):
        total_kops_1 = self.rub * 100 + self.kop
        total_kops_2 = money2.rub * 100 + money2.kop
        return total_kops_1 == total_kops_2

    def __ne__(self, money2):
        return not self.__eq__(money2)

    def __mod__(self, percent):
        total_kops = self.rub * 100 + self.kop
        total_kops = round(total_kops // 100 * percent)
        total_rub = total_kops // 100
        total_kop = total_kops % 100
        return f"{total_rub} руб. {total_kop:02} коп."

    def convert(self, currency="USD"):
        data = urllib.request.urlopen(URL).read()
        data_dict = json.loads(data)
        if currency == "USD":
            exchange_rate = data_dict["Valute"]["USD"]["Value"]
        elif currency == "EUR":
            exchange_rate = data_dict["Valute"]["EUR"]["Value"]
        else:
            # В случае неправильно указанной валюты возвращаем значение 1:1
            exchange_rate = 1
        total_rubs = self.rub + self.kop / 100
        return round(total_rubs / exchange_rate, 2)


some_money_1 = Money(162, 24)
some_money_2 = Money(24, 12)

print(f"Даны две суммы: {some_money_1} и {some_money_2}")
print(f"Проверка суммы: {some_money_1} + {some_money_2} = {some_money_1 + some_money_2}")
print(f"Проверка разности: {some_money_1} - {some_money_2} = {some_money_1 - some_money_2}")
print(f"Проверка умножения: {some_money_1} * 3 = {some_money_1 * 3}")
print("Сравнение сумм: ", end="")
if some_money_1 > some_money_2:
    print(f"{some_money_1} больше, чем {some_money_2}")
else:
    print(f"{some_money_1} меньше, чем {some_money_2}")
print("Сравнение равенства сумм: ", end="")
if some_money_1 == some_money_2:
    print(f"{some_money_1} равна {some_money_2}")
else:
    print(f"{some_money_1} не равна {some_money_2}")
print("Сравнение неравенства сумм: ", end="")
if some_money_1 != some_money_2:
    print(f"{some_money_1} не равна {some_money_2}")
else:
    print(f"{some_money_1} равна {some_money_2}")
print(f"Проверка процента от суммы: {some_money_1} % 20 = {some_money_1 % 20}")
print(f"Проверка перевода суммы в доллары: {some_money_1} составляет {some_money_1.convert()} долларов США")
conv_eur = some_money_1.convert("EUR")
print(f"Проверка перевода суммы в евро: {some_money_1} составляет {conv_eur} евро")

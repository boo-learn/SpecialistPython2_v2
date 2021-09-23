import random
import requests


class Money:

    def __init__(self, rub, cent):
        self.rub = rub
        self.cent = cent

    def count_sum(self):
        full_sum = (self.rub * 100) + self.cent
        rubli = full_sum // 100
        cent = full_sum % 100
        return rubli, cent

    def __str__(self):
        return f'{self.count_sum()[0]}руб {self.count_sum()[1]}коп'

    def __add__(self, other_sum):
        return Money(self.rub + other_sum.rub, self.cent + other_sum.cent)

    def __sub__(self, other_sum):
        return Money(self.rub - other_sum.rub, self.cent - other_sum.cent)

    def __mul__(self, other_sum):
        return Money(self.rub * other_sum.rub, self.cent * other_sum.cent)

    def __gt__(self, other_sum):
        if True:
            return (self.rub * 100) + self.cent > (other_sum.rub * 100) + other_sum.cent
        else:
            return (self.rub * 100) + self.cent < (other_sum.rub * 100) + other_sum.cent

    def __lt__(self, other_sum):
        if True:
            return (self.rub * 100) + self.cent < (other_sum.rub * 100) + other_sum.cent
        else:
            return (self.rub * 100) + self.cent > (other_sum.rub * 100) + other_sum.cent

    def __le__(self, other_sum):
        if True:
            return (self.rub * 100) + self.cent <= (other_sum.rub * 100) + other_sum.cent
        else:
            return (self.rub * 100) + self.cent >= (other_sum.rub * 100) + other_sum.cent

    def __ge__(self, other_sum):
        if True:
            return (self.rub * 100) + self.cent >= (other_sum.rub * 100) + other_sum.cent
        else:
            return (self.rub * 100) + self.cent <= (other_sum.rub * 100) + other_sum.cent

    def __eq__(self, other_sum):
        return (self.rub * 100) + self.cent == (other_sum.rub * 100) + other_sum.cent

    def __ne__(self, other_sum):
        return (self.rub * 100) + self.cent != (other_sum.rub * 100) + other_sum.cent

    def __mod__(self, percent):
        return Money(0, (self.rub * 100 + self.cent) * percent // 100)

    def convert(self):
        url = f'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        response_to_eur = response.json()['Valute']['EUR']['Value']
        response_to_usd = response.json()['Valute']['USD']['Value']
        return f'Cумма {self} \n EUR:{response_to_eur} \n USD:{response_to_usd}'


"""
Проверка на арефметические и логические операции
"""
list_coin = []
for amount in range(5):
    list_coin.append(random.randint(10, 100))
    first = list_coin[0]
    for char in list_coin[1:]:
        second = char
        money_sum1 = Money(first, second)
        first = second
        money_sum2 = Money(first, second)
        money_result = money_sum1 + money_sum2  # Складываем суммы
        print(money_result)  # 31руб 5коп
        money_result = money_sum1 - money_sum2  # Вычитаем суммы
        print(money_result)  # 10руб 15коп
        money_result = money_sum1 * money_sum2  # Умножение суммы
        print(money_result)
        if money_sum1 > money_sum2:
            print(f'Сумма {money_sum1} больше, чем сумма {money_sum2}')
        else:
            print(f'Сумма {money_sum1} меньше, чем сумма {money_sum2}')

        if money_sum1 < money_sum2:
            print(f'Сумма {money_sum1} меньше, чем сумма {money_sum2}')
        else:
            print(f'Сумма {money_sum1} больше, чем сумма {money_sum2}')

        if money_sum1 >= money_sum2:
            print(f'Сумма {money_sum1} больше или равна сумме {money_sum2}')
        else:
            print(f'Сумма {money_sum1} меньше, чем сумма {money_sum2}')

        if money_sum1 <= money_sum2:
            print(f'Сумма {money_sum1} меньше или равна сумме {money_sum2}')
        else:
            print(f'Сумма {money_sum1} больше, чем сумма {money_sum2}')

        if money_sum1 == money_sum2:
            print(f'Сумма {money_sum1} равна сумме {money_sum2}')
        else:
            print(f'Сумма {money_sum1} не равна сумме {money_sum2}')

        if money_sum1 != money_sum2:
            print(f'Сумма {money_sum1} не равна сумме {money_sum2}')
        else:
            print(f'Сумма {money_sum1} равна сумме {money_sum2}')

# Проверка на вычисление процента от суммы
print("*****"*5)
sum1 = Money(20, 60)
print(sum1 % 21)
# Конвертация в валюту
print("*****"*5)
print(sum1.convert())

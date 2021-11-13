import json
import urllib.request


class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def sum_kop(self):
        return self.rub * 100 + self.kop

    def __repr__(self):
        return f'{self.sum_kop() // 100}руб {self.sum_kop() % 100}коп'

    def __add__(self, other):
        new_sum = Money.sum_kop(self) + Money.sum_kop(other)
        return Money(new_sum // 100, new_sum % 100)

    def __sub__(self, other):
        new_sum = Money.sum_kop(self) - Money.sum_kop(other)
        return Money(new_sum // 100, new_sum % 100)

    def __mul__(self, num):
        new_sum = Money.sum_kop(self) * num
        return Money(new_sum // 100, new_sum % 100)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        return Money.sum_kop(self) > Money.sum_kop(other)

    def __lt__(self, other):
        return not self > other

    def __eq__(self, other):
        return Money.sum_kop(self) == Money.sum_kop(other)

    def __ne__(self, other):
        return Money.sum_kop(self) != Money.sum_kop(other)

    def percent(self, percent):
        new_result = round(Money.sum_kop(self) * percent / 100)
        return Money(new_result // 100, new_result % 100)

    def convert(self, currency):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        val = data_dict["Valute"][currency]["Value"]
        result = round(Money.sum_kop(self) / val / 100, 2)
        return Money(int(result), int(result % 1 * 100))



money = Money(1000, 00)
print(money.convert('EUR'))


money = Money(25, 120)

print(money)



money_1 = Money(20, 60)
money_2 = Money(10, 45)


money_result = money_1 + money_2
print(money_result)  # 31руб 5коп
money_result = money_1 - money_2
print(money_result) # 10руб 15коп

money_result = money_1 * 2
print (money_result)
money_result = 2 * money_1
print (money_result)

# if money_1 > money_2:
#     print(f'{money_1} больше чем {money_2}')
# else:
#     print(f'{money_1} меньше чем {money_2}')

# print(money_1 < money_2)
# print(money_2 < money_1)
# print(money_1 == money_2)
# print(money_2 != money_1)
#
print(money_2.percent(21))



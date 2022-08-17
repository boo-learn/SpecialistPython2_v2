import urllib.request
import json


class Money:
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __init__(self, rubles, kopecks):
        self.rubles = rubles
        self.kopecks = kopecks

    def __str__(self):
        rubles = self.rubles + self.kopecks // 100
        kopecks = self.kopecks % 100
        return f'{rubles} руб {kopecks} коп'

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.kopecks + other.kopecks)

    def __sub__(self, other):
        return Money(self.rubles - other.rubles, self.kopecks - other.kopecks)

    def __mul__(self, other):
        return Money(self.rubles * other, self.kopecks * other)

    def __gt__(self, other): # >
        return self.rubles + self.kopecks / 100 > other.rubles + other.kopecks / 100

    def __lt__(self, other): # <
        return not self.__gt__(other)

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mod__(self, other):
        money = (self.rubles + self.kopecks / 100) * other
        rubles = money // 100
        kopecks = money % 100
        return Money(round(rubles), round(kopecks))

    def convert(self, currency): # currence -> "USD"/"EUR"

        data = urllib.request.urlopen(Money.url).read()
        data_dict = json.loads(data)
        return f'Сумма в {currency} состравляет: ' \
               f'{round((self.rubles + self.kopecks) / data_dict["Valute"][currency]["Value"], 2)}'


money_sum1 = Money(20, 55)
money_sum2 = Money(10, 45)
money_sum3 = Money(20, 130)
print(f'Первая сумма {money_sum1}')
print(f'Вторая сумма {money_sum2}')

money_result_add = money_sum1 + money_sum2
print(f'Сумма сумм {money_result_add}')

money_result_sub = money_sum1 - money_sum2
print(f'Разность сумм {money_result_sub}')

money_result_mul = money_sum1 * 2
print(f'Умножение на целое число {money_result_mul}')

if money_sum1 > money_sum2:
    print(f'{money_sum1} больше {money_sum2}')
else:
    print(f'{money_sum1} меньше {money_sum2}')

if money_sum1 == money_sum3:
    print(f'{money_sum1} равен {money_sum3}')
else:
    print(f'{money_sum1} не равен {money_sum3}')

money_sum4 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money_sum2 % 21

print(percent_sum)  # 4руб 33ко

money_sum5 = Money(100, 80)
print(money_sum5.convert('USD'))
print(money_sum5.convert('EUR'))

import json
import urllib.request


class Money:
    def __init__(self, rubles, kopek, currency='RUR'):
        self.ruble_value = rubles + kopek // 100
        self.kopek_value = kopek % 100
        self.currency = currency

    def as_kopek(self):
        return self.ruble_value * 100 + self.kopek_value

    def __str__(self):
        if self.currency == 'RUR':
            return f"{self.ruble_value} руб. {self.kopek_value} коп."
        else:
            return f"{self.currency} {self.ruble_value}.{self.kopek_value} "

    def __add__(self, other):
        return Money(self.ruble_value + other.ruble_value, self.kopek_value + other.kopek_value, self.currency)

    def __sub__(self, other):
        return Money(0, self.as_kopek - other.as_kopek, self.currency)

    def __mul__(self, other):
        return Money(0, self.as_kopek() * other, self.currency)

    def __eq__(self, other):
        return self.as_kopek() == other.as_kopek()

    def __lt__(self):
        return self.as_kopek() < other.as_kopek()

    def __gt__(self):
        return self.as_kopek() > other.as_kopek()

    def __mod__(self, other):
        res = round((self.ruble_value * 100 + self.kopek_value) / 100 * other)
        return Money(0, res, self.currency)

    def convert(self, currency):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        currency_rate = data_dict['Valute'][currency]['Value']

        value_in_currency = round((self.ruble_value * 100 + self.kopek_value) / currency_rate)
        convert_sum = Money(0, value_in_currency)
        convert_sum.currency = currency

        return convert_sum


# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1)  # 21руб 20коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

# Доп.задание
# Добавьте операцию - вычисление процент от суммы.
# Создаем две денежные суммы
money_sum1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money_sum1 % 21
print(percent_sum)  # 4руб 33коп

convert_sum = money_sum1.convert('USD')
print(f"Сконвертированная сумма {convert_sum}")

convert_sum = convert_sum * 3
print(f"Сконвертированная сумма {convert_sum}")

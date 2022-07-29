import json
import urllib.request

class Money:

    USD = 'USD'
    EUR = 'EUR'

    def __init__(self, rubles, kopeiks=0):

        self.rubles = rubles
        self.kopeiks = kopeiks
        self.total_amount = float ( self.rubles + self.kopeiks / 100 )

    def __str__(self):

        return f'{int(self.total_amount // 1)} руб. {int(round((self.total_amount % 1 * 100),0))} коп.'

    def __add__(self, other_amount):

        self.money_sum = self.total_amount + other_amount.total_amount

        return Money(int(self.money_sum // 1), int(round((self.money_sum % 1 * 100),0)))

    def __sub__(self, other_amount):

        self.money_diff = self.total_amount - other_amount.total_amount

        return Money(int(self.money_diff // 1), int(round((self.money_diff % 1 * 100),0)))

    def __mul__(self, x: int):

        self.money_mult = self.total_amount * x

        return Money(int(self.money_mult // 1), int(round((self.money_mult % 1 * 100),0)))

    def __eq__(self, other_amount):

        return self.total_amount == other_amount.total_amount

    def __gt__(self, other_amount):

        return self.total_amount > other_amount.total_amount

    def __lt__(self, other_amount):

        return self.total_amount < other_amount.total_amount

    def __mod__(self, x):

        self.percentage = self.total_amount * (x/100)

        return Money(int(self.percentage // 1), int(round((self.percentage % 1 * 100),0)))

    def convert(self, currency):

        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)

        currency_rate = data_dict['Valute'][currency]['Value']

        self.conveted_amount = self.total_amount / currency_rate

        return f'сконвертированная сумма {round(self.conveted_amount, 2)} {currency}'

# ТЕСТИРОВАНИЕ

# Создаем два объекта Money ()
money1 = Money(2,50)
money2 = Money(3,0)

# Тестируем строкое представление
print("Тестируем строкое представление")
print(money1)

# Складываем, выводим результат
money_sum = money1 + money2
print("Складываем, выводим результат")
print(money_sum)

# Результат любого из действий может использоваться как самостоятельный объект
money_sum += money_sum
print("Результат любого из действий может использоваться как самостоятельный объект")
print(money_sum)

# Можно выводить на печать без дополнительных переменных
print("Можно выводить на печать без дополнительных переменных")
print(money2-money1)

# умножение на целое число
print("Умножение на целое число")
print(money1*2)

# расчет процента как в примере
money1 = Money(20,60)
percent_sum = money1 % 21
print('Расчет процента как в примере')
print(percent_sum)

# Больше, меньше, равно
print("Больше, меньше, равно")
print(f'суммы равны? {money1 == money2}')
print(f'первая сумма больше второй? {money1 > money2}')
print(f'первая сумма меньше второй? {money1 < money2}')

# Конвертация в валюту

money1 = Money(5573, 00)
money2 = Money(12532)

to_usd = money1.convert(Money.USD)
to_eur = money2.convert(Money.EUR)
print('Конвертация в валюту')
print(to_usd)
print(to_eur)

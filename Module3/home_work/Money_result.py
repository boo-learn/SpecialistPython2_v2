import json
import urllib.request
from pprint import pprint

class Money:
    def __init__(self, bills, cents):
        self.cents = bills*100 + cents

    def __repr__(self):
        bills, cents = Money.all_sum(self.cents)
        return f"{bills} руб. {cents} коп."

    @staticmethod
    def all_sum(self_cents):
        bills = self_cents // 100
        cents = self_cents % 100
        return (bills, cents)

    def __add__(self, other):
        sum_cents = self.cents + other.cents
        return Money(*Money.all_sum(sum_cents))

    def __sub__(self, other):
        sum_cents = self.cents - other.cents
        return Money(*Money.all_sum(sum_cents))

    def __mul__(self, num):
        sum_cents = self.cents * num
        return Money(*Money.all_sum(sum_cents))

    def __rmul__(self, num):
        sum_cents = self.cents * num
        return Money(*Money.all_sum(sum_cents))

    def __eq__(self, other):
        return self.cents == other.cents

    def __ne__(self, other):
        return self.cents != other.cents

    def __gt__(self, other):
        return self.cents > other.cents

    def __lt__(self, other):
        return self.cents < other.cents

    def __le__(self, other):
        return self.cents <= other.cents

    def __ge__(self, other):
        return self.cents >= other.cents


    def __mod__(self, other):
        percent = round(self.cents * other/100)
        return Money(*Money.all_sum(percent))


    def convert(self):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        one_eur_cents = data_dict['Valute']['EUR']['Value']*100
        one_usd_cents = data_dict['Valute']['EUR']['Value']*100
        return f'За {Money.all_sum(self.cents)} можно купить {round((self.cents/one_eur_cents),2)} Евро или {round((self.cents/one_usd_cents),2)} Долларов.'



# Создаем сумму из 20 рублей и 120 копеек
money_sum = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum) # 21руб 20коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп



# Находим 21% от суммы
percent_sum = money_sum1 % 21

print(percent_sum)  # 4руб 33коп

# Конвертируем рубли в Евро и Доллары

pprint(money_sum1.convert())


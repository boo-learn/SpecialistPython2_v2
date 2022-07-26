import urllib.request
import json


class Money:
    def __init__(self, ruble, penny):
        self.ruble = ruble
        self.penny = penny

    def penny_to_rubles(self):
        if self.penny >= 100:
            to_rubles = self.penny // 100
            self.ruble += to_rubles
            self.penny -= to_rubles * 100
        return Money(self.ruble, self.penny)

    def __str__(self):
        return f"{self.penny_to_rubles().ruble}руб {self.penny_to_rubles().penny}коп"

    def __add__(self, other):
        sum_rub = self.penny_to_rubles().ruble + other.penny_to_rubles().ruble
        sum_penny = self.penny_to_rubles().penny + other.penny_to_rubles().penny
        final_sum = Money(sum_rub, sum_penny)
        return final_sum

    def __mod__(self, other):
        remain = (self.penny_to_rubles().ruble * other) % 100
        return Money(self.penny_to_rubles().ruble * other // 100,
                     round(self.penny_to_rubles().penny * other / 100 + remain)).penny_to_rubles()

    def convert(self):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        usd = data_dict.get('Valute').get('USD').get('Value')
        eur = data_dict.get('Valute').get('EUR').get('Value')
        return f'USD: {round((self.penny_to_rubles().ruble + self.penny_to_rubles().penny * 0.01) / usd, 2)}\n' \
               f'EUR: {round((self.penny_to_rubles().ruble + self.penny_to_rubles().penny * 0.01) / eur, 2)}'


money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
money_result = money_sum1 + money_sum2
print(money_result) # Выводим результат сложения
percent_sum = money_sum1 % 21
print(percent_sum) # Выводим процент от суммы
print(money_sum1.convert()) # Выводим конвертацию в евро и доллары

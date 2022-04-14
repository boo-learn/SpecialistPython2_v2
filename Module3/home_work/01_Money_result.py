import urllib.request
import json


class Money:
    def __init__(self, big, little):
        self.big = big
        self.little = little
        self.kopeiki_v_rubli()

    def kopeiki_v_rubli(self):
        if (self.little % 100 < 100):
            self.big += self.little // 100
            self.little = self.little % 100

    def __str__(self):
        return f"{self.big}руб {self.little}коп"

    def __add__(self, sredstva):
        sum_rubli = self.big + sredstva.big
        sum_kopeiki = self.little + sredstva.little
        itogo = Money(sum_rubli, sum_kopeiki)
        return itogo

    def __mod__(self, input_percent):
        return Money(0, int(round((self.big * 100 + self.little) * input_percent / 100, 0)))

    def convert(self, kod_simvola):
        data = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
        data_dict = json.loads(data)

        list_1 = []  # список чтобы сохранить в него все данные по ключю - коду символу
        for key, value in data_dict.items():
            if type(value) == dict:
                for key_2, value2 in value.items():
                    if key_2 == kod_simvola:
                        for key_3, value_3 in value2.items():
                            list_1.append(value_3)
        return f"На сумму {str(self)} " \
               f"Можно купить: {round((self.big * 100 + self.little) / (float(list_1[5]) * 100), 4)}" \
               f" {(list_1[4])}"


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

# Создаем две денежные суммы
money_sum1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money_sum1 % 21

print(percent_sum)  # 4руб 33коп

money_sum1 = Money(100, 50)
# Список ключей вложенного словаря, получаемого в запросе,
# онже является кодом символа для перевода
# dict_keys(['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL',
#            'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT',
#            'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON',
#            'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH',
#            'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY'])
kod_simvola = "EUR"  # вводим код символа для конвертации
print(money_sum1.convert(kod_simvola))  # передаем сумму и код

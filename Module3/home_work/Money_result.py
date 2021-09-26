import requests
import datetime
class Money:
    def __init__(self, rub, kopeiki):
        self.rub = rub
        self.kopeiki = kopeiki
        if self.kopeiki > 99:
            self.rub = self.rub + kopeiki // 100
            self.kopeiki = self.kopeiki % 100
    # TODO: your code here

    def __str__(self):
        return f'{self.rub}руб {self.kopeiki}коп'

    def __add__(self, other_money):
        kopeiki_sum = self.kopeiki + other_money.kopeiki
        return Money(self.rub + other_money.rub + (kopeiki_sum)//100, kopeiki_sum%100)

    def __mod__(self, percent):
        common_kop = (self.rub*100 +self.kopeiki) * (percent/100)
        kop = (common_kop%100)
        return Money(int(common_kop // 100), round(kop))

    def __currency_today(self,valute):  # 2021/09/23
        year, month, day = datetime.date.today().__str__().split('-')
        url = f"https://www.cbr-xml-daily.ru/archive/{year}/{month}/{int(day) - 1}/daily_json.js"# на текуший день нет данных
        # url = "https://www.cbr.ru/currency_base/daily/"
        response = requests.get(url)
        data_dict = response.json()
        # print(data_dict['Valute'][f'{valute.upper()}']['Value'])
        return float(data_dict['Valute'][f'{valute.upper()}']['Value'])

    def convert(self,valute):
        print(self.rub + self.kopeiki/100)
        print(self.__currency_today(valute))
        common_kop = (self.rub*100 + self.kopeiki/100) / self.__currency_today(valute)
        kop = (common_kop % 100)
        print(kop)
        return f"{int(common_kop // 100)}.{round(kop)} {valute.upper()}"




# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1) # 21руб 20коп
# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

# Находим 21% от суммы
percent_sum = money_sum1 % 21
print(percent_sum)  # 4руб 33коп

valute = money_sum1.convert('eur')
print(valute)

import urllib.request
import json

class Money:
    def __init__(self, rubles, kopecks=0):
        self.rubles = rubles
        self.kopecks = kopecks
        self.__kopecks = rubles * 100 + kopecks
        if self.kopecks >= 100:
            self.rubles += self.kopecks // 100
            self.kopecks %= 100

    def __str__(self):
        if self.rubles >= 0:
            return f"{self.rubles}руб {self.kopecks}коп"
        else:
            return f"-{abs(self.rubles)}руб {abs(self.kopecks)}коп"

    def __add__(self, other):
        rubles = self.rubles + other.rubles
        kopecks = self.kopecks + other.kopecks
        return Money(rubles, kopecks)

    def __sub__(self, other):
        rubles = self.rubles - other.rubles
        kopecks = self.kopecks - other.kopecks
        return Money(rubles, kopecks)

    def __mul__(self, number):
        rubles = self.rubles * number
        kopecks = self.kopecks * number
        return Money(rubles, kopecks)

    def __mod__(self, percent):
        total_kopeks = self.rubles * 100 + self.kopecks
        percent_sum = total_kopeks * percent / 100
        rubles = int(percent_sum // 100)
        kopecks = int(round(percent_sum % 100))
        return Money(rubles, kopecks)

    def convert(self, dollar):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        euro_rate = data_dict["Valute"]["EUR"]["Value"]
        dollar_rate = data_dict["Valute"]["USD"]["Value"]
        euro = (self.rubles + self.kopecks / 100) / euro_rate
        dollar = (self.rubles + self.kopecks / 100) / dollar_rate
        return f"{euro:.2f} евро, {dollar:.2f} долларов"

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __lt__(self, other):
        return self.rubles < other.rubles or (self.rubles == other.rubles and self.kopecks < other.kopecks)

    def __gt__(self, other):
        return self.rubles > other.rubles or (self.rubles == other.rubles and self.kopecks > other.kopecks)

# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1)  # 21руб 20коп
#
# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
#
# # Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
money_result_minus = money_sum2 - money_sum1
print(money_result_minus) # -10руб 15коп

# Находим 21% от суммы
money_sum3 = Money(20, 60)
percent_sum = money_sum3 % 21
print(percent_sum)  # 4руб 33

money_sum1 = Money(20, 120) # 21руб 20коп
print(money_sum1.convert("")) # 0.24 евро, 0.26 долларов

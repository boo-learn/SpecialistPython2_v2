import urllib.request
import json


class Money:

    def __init__(self, rubles=0, coins=0):
        self.__sum = rubles * 100 + coins

    def __str__(self):
        # if self.convert("USD"):
        #     return "{}.{} USD.".format(self.__sum // 100, self.__sum % 100)
        # elif self.convert("EUR"):
        #     return "{}.{} EUR.".format(self.__sum // 100, self.__sum % 100)
        return "{} руб. {} коп.".format(self.__sum // 100, self.__sum % 100)

    def __add__(self, other_money):
        return Money(0, self.__sum + other_money.__sum)

    def __sub__(self, other_money):
        return Money(0, self.__sum - other_money.__sum)

    def __mul__(self, number):
        return Money(0, self.__sum * number)

    def __eq__(self, other_money):
        return self.__sum == other_money.__sum

    def __gt__(self, other_money):
        return self.__sum > other_money.__sum

    def __mod__(self, percent):
        return Money(0, round(self.__sum * percent / 100))

    def convert(self, valute):
        if valute == "USD":
            return Money(0, round(self.__sum / data_dict["Valute"]["USD"]["Value"]))
        elif valute == "EUR":
            return Money(0, round(self.__sum / data_dict["Valute"]["EUR"]["Value"]))


data = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
data_dict = json.loads(data)

money_sum1 = Money(120, 60)
money_sum2 = Money(10, 20)
money_sum3 = Money(10, 120)
money_sum4 = Money(10, 120)

money_result_add = money_sum1 + money_sum2
money_result_sub = money_sum3 - money_sum4
money_result_mul = money_sum1 * 2

print('Первая сумма:', money_sum1)
print('Вторая сумма:', money_sum2)
print('Третья сумма:', money_sum3)
print('Четвертая сумма:', money_sum4)

print(f"Сложение {money_sum1} и {money_sum2}:", money_result_add)
print(f"Вычитание {money_sum3} и {money_sum4}:", money_result_sub)
print(f"Умножение {money_sum1} на 2:", money_result_mul)
print(f"Равны ли суммы {money_sum3} и {money_sum4}:", money_sum3 == money_sum4)
print(f"Больше ли {money_sum1} чем {money_sum2}:", money_sum1 > money_sum2)
print(f"50% от {money_sum2}:", money_sum2 % 50)
print(f"21% от {money_sum1}:", money_sum1 % 21)

print(money_sum1.convert('EUR'))
print(money_sum2.convert('USD'))

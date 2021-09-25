###Последняя версия

import requests


class Money:
    def __init__(self, rub, kop):
        self.rub = rub + kop // 100
        self.kop = kop % 100

    def __str__(self):
        return f'{self.rub}руб {self.kop}коп'

    def __add__(self, other):
        return Money(self.rub + other.rub,
                     other.kop + self.kop)

    def __sub__(self, other): # не работает со знаком "-"
        sub_money = (self.rub * 100 + self.kop) - (other.rub * 100 + other.kop)
        rub_sub = abs(sub_money) // 100
        kop_sub = abs(sub_money) % 100
        return Money(rub_sub, kop_sub)

    def __mul__(self, mul):
        return Money(self.rub * mul,
                     self.kop * mul)

    def __gt__(self, other):
        return (self.rub * 100 + self.kop) > (other.rub * 100 + other.kop)

    def __eq__(self, other):
        return (self.rub * 100 + self.kop) == (other.rub * 100 + other.kop)

    def percent(self, per):
        percent_summ = round(((self.rub * 100 + self.kop) * per) / 100)
        rub_sum = percent_summ // 100
        kop_sum = percent_summ % 100
        return f'{rub_sum}руб {kop_sum}коп'

    def convert(self, valute):
        valute = valute.upper()
        url = f"https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        curse = data['Valute'][valute]['Value']
        money_convert = round(((self.rub + self.kop / 100) / curse), 2)
        return f'{money_convert} {valute}'

# Примеры:
# # Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
print('money_sum1=', money_sum1)
# Создаем денежные суммы
money_sum2 = Money(10, 158)
print('money_sum2=', money_sum2)
money_sum3 = Money(123, 121)
print('money_sum3=', money_sum3)
money_sum4 = Money(123, 121)
money_sum5 = money_sum1 + money_sum2
print('money_sum5=', money_sum5)
# print('money_sum3=', money_sum3)
# print('money_sum4=', money_sum4)
# print('money_sum5=', money_sum5)
money_sum5 *= 2
print('money_sum5 * 2 =', money_sum5)
# # # Складываем суммы
money_result1 = money_sum1 + money_sum2
print('money_sum1 + money_sum2=', money_result1)
# # # Вычитаем суммы
money_sum6 = money_sum5 - money_sum1
print(money_sum5, '-', money_sum1, '=', money_sum6)
money_sum7 = money_sum1 - money_sum5
print(money_sum1, '-' ,money_sum5, '=', money_sum7)
money_sum8 = money_sum7 - money_sum1
print(money_sum7, '-' ,money_sum1, '=', money_sum8)
# money_result2 = money_sum1 - money_sum2
# money_result3 = money_sum2 - money_sum1
# print('money_sum1 - money_sum2=', money_result2)
# print('money_sum2 - money_sum1=', money_result3)
# # # Умножение на целое число
# money_result4 = money_sum1 * 10
# money_result5 = money_sum2 * 51
# print('money_sum1 * 10=', money_result4)
# print('money_sum2 * 51=', money_result5)
# # # Сравнение больше >
if money_sum1 > money_sum2:
    print(f"{money_sum1} больше {money_sum2}")
elif money_sum1 < money_sum2:
    print(f"{money_sum1} меньше {money_sum2}")
# # Сравнение меньше <
if money_sum2 < money_sum1:
    print(f"{money_sum2} меньше {money_sum1}")
elif money_sum2 > money_sum1:
    print(f"{money_sum2} больше {money_sum1}")
# # Сравнение =
if money_sum2 == money_sum1:
    print(f"{money_sum2} равно {money_sum1}")
elif money_sum2 != money_sum1:
    print(f"{money_sum2} не равно {money_sum1}")
# # Сравнение !=
if money_sum3 != money_sum4:
    print(f"{money_sum3} не равно {money_sum4}")
elif money_sum3 == money_sum4:
    print(f"{money_sum3} равно {money_sum4}")
# # Процент
percent1 = money_sum5.percent(10)
print(money_sum5, '=', percent1, '(10%)')
print(money_sum1, '=', money_sum1.percent(10), '(10%)')
print(money_sum2, '=', money_sum2.percent(20), '(20%)')
print(money_sum3, '=', money_sum3.percent(30), '(30%)')
print(money_sum4, '=', money_sum4.percent(40), '(40%)')
# Конвертация
money_convert1 = money_sum1.convert("eur")
money_convert2 = money_sum2.convert("usd")
money_convert3 = money_sum3.convert("nok")
print(money_sum1, money_convert1, sep='->')
print(money_sum2, money_convert2, sep='->')
print(money_sum3, money_convert3, sep='->')

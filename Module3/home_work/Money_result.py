import requests


class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        self.rub = self.rub + self.kop // 100
        self.kop = self.kop % 100
        return f'{self.rub}руб {self.kop}коп'

    def __add__(self, other):
        money_sum = self.rub * 100 + other.rub * 100 + other.kop + self.kop
        rub_sum = money_sum // 100
        kop_sum = money_sum % 100
        return f'{rub_sum}руб {kop_sum}коп'

    def __sub__(self, other):
        money_sum = self.rub * 100 - other.rub * 100 + self.kop - other.kop
        rub_sum = money_sum // 100
        kop_sum = money_sum % 100
        return f'{rub_sum}руб {kop_sum}коп'

    def __mul__(self, mul):
        money_mul = (self.rub * 100 + self.kop) * mul
        rub_sum = money_mul // 100
        kop_sum = money_mul % 100
        return f'{rub_sum}руб {kop_sum}коп'

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
# Создаем денежные суммы
money_sum2 = Money(10, 158)
money_sum3 = Money(123, 121)
money_sum4 = Money(123, 121)
money_sum5 = Money(152, 10)
print('money_sum1=', money_sum1)
print('money_sum2=', money_sum2)
print('money_sum3=', money_sum3)
print('money_sum4=', money_sum4)
print('money_sum5=', money_sum5)
# # # Складываем суммы
money_result1 = money_sum1 + money_sum2
print('money_sum1 + money_sum2=', money_result1)
# # Вычитаем суммы
money_result2 = money_sum1 - money_sum2
money_result3 = money_sum2 - money_sum1
print('money_sum1 - money_sum2=', money_result2)
print('money_sum2 - money_sum1=', money_result3)
# # Умножение на целое число
money_result4 = money_sum1 * 10
money_result5 = money_sum2 * 51
print('money_sum1 * 10=', money_result4)
print('money_sum2 * 51=', money_result5)
# # Сравнение больше >
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

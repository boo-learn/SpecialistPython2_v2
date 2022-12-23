import urllib.request
import json


def get_rate(valuta_id,
             url="https://www.cbr-xml-daily.ru/daily_json.js"):
    data = urllib.request.urlopen(url).read()
    data_dict = json.loads(data)
    valute = data_dict.get("Valute").get(valuta_id)
    if valute:
        return valute.get("Value")
    else:
        print(f'Валюта не найдена: "{valuta_id}"')
        return


class Money:
    def __init__(self, rubles, kopecks):
        self.value = rubles * 100 + kopecks  # все операции в копейках

    # представление с наименьшим числом копеек
    # вопрос с __repr__ тоже работал print, в чем разница?
    def __str__(self):
        if self.value >= 0:
            rubles, kopecks = self.value // 100, self.value % 100
            return (f"{rubles}руб {kopecks}коп")
        else:
            rubles_float = abs(self.value / 100)
            rubles = int(rubles_float)
            kopecks = int((rubles_float - rubles) * 100)
            return (f"-{rubles}руб {kopecks}коп")

    # сложение
    def __add__(self, other):
        return Money(0, self.value + other.value)

    # вычитание
    def __sub__(self, other):
        return Money(0, self.value - other.value)

    # умножение на число
    def __mul__(self, other):
        return Money(0, round(self.value * other))

    def __rmul__(self, other):  # обеспечиваем перемену мест множителей
        return Money(0, round(self.value * other))

    # сравнение:
    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __mod__(self, other):
        return Money(0, round((self.value / 100) * other))

    # конвертация
    def convert(self, valuta_id):  # конвертация в евро и доллары request + json
        if valuta_id in ("USD", "EUR"):
            rate = get_rate(valuta_id)
        else:
            print(f'Конвертация в валюту не поддерживается: "{valuta_id}"')
            return
        val = round((self.value / 100) / rate, 2)
        return val


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
print(money_sum2 + money_sum1)

# проверяем вычитание
money_sum1 = Money(0, 101)
money_sum2 = Money(0, 208)
print(money_sum1 - money_sum2)
print(money_sum2 - money_sum1)

# проверяем умножение на число
money_sum1 = Money(1, 1)
print(money_sum1 * 100)
print(0.1 * money_sum1)

# проверяем процент от суммы
money_sum1 = Money(100, 1000)
print(money_sum1 % 10)

# проверяем конвертацию
money_sum1 = Money(1000, 0)
print(money_sum1.convert("EUR"))
print(money_sum1.convert("USD"))
print(money_sum1.convert("GBP"))


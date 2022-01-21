class Money:
    def __init__(self, rub, kop):
        self.rub = int(rub + kop // 100)
        self.kop = kop % 100

    def to_kop(self):
        return self.rub * 100 + self.kop

    def to_norm(self):
        r = self.rub + self.kop // 100
        k = self.kop % 100
        x = Money(r, k)
        return x

    def __add__(self, other):
        x = self.to_kop()
        y = other.to_kop()
        res = x + y
        return Money(0, res)


    def __sub__(self, other):
        x = self.to_kop()
        y = other.to_kop()
        res = x - y
        return Money(0, res)

    def __mul__(self, value):
        x = self.to_kop()
        res = x * value
        return Money(0, res)

    def __truediv__(self, value):
        x = self.to_kop()
        res = x / value
        return Money(0, res)

    def __mod__(self, value):
        x = self.to_kop()
        res = x * 0.01 * value
        return Money(0, res)

    def __it__(self, other):
        x = self.to_kop()
        y = other.to_kop()
        return x < y

    def __gt__(self, other):
        x = self.to_kop()
        y = other.to_kop()
        return x > y

    def __eq__(self, other):
        x = self.to_kop()
        y = other.to_kop()
        return x == y

    def __ne__(self, other):
        x = self.to_kop()
        y = other.to_kop()
        return x != y

    def __repr__(self):
        return f"{self.rub}руб {self.kop:.0f}коп"

    def convert(self, valute: str):
        import urllib.request, json
        url = r"https://www.cbr-xml-daily.ru/daily_json.js"
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        rate = data_dict['Valute'][valute.upper()]["Value"]
        conv = self / rate
        return Valute(conv.rub, conv.kop, valute.upper())


class Valute(Money):
        def __init__(self, rub, kop, valute):
        Money.__init__(self, rub, kop)
        self.valute = valute

    def __repr__(self):
        if self.valute == "USD":
            return f"{self.rub}.{self.kop:.0f} $"
        elif self.valute == "EUR":
            return f"{self.rub}.{self.kop:.0f} Eur"



if __name__ == '__main__':
    money_sum1 = Money(20, 120)
    print(money_sum1)

    money_sum1 = Money(150, 33)
    money_sum2 = Money(10, 45)
    money_result = money_sum1 + money_sum2
    print(money_sum1, money_sum2)
    print("Сумма: ", money_result)
    print("Разность: ", money_sum1 - money_sum2)
    print("Умножение на 2: ", money_sum1 * 2)
    print("Деление на 2: ", money_sum1 / 2)
    print("30% от суммы: ", money_sum1 % 30)

    print("sum1 < sum2: ", money_sum1 < money_sum2)
    print("sum1 > sum2: ", money_sum1 > money_sum2)
    print("sum1 == sum2: ", money_sum1 == money_sum2)
    print("sum1 != sum2: ", money_sum1 != money_sum2)


    valute = "usd"
    res = money_sum1.convert(valute)
    print(f"{money_sum1} в {valute} равно {res}")
    valute = "Eur"
    res = money_sum1.convert(valute)
    print(f"{money_sum1} в {valute} равно {res}")

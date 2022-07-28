import urllib.request


def sign(amt):
    if amt >= 0:
        return 1
    else:
        return -1


class Money:
    # currency_dict = {'RUB': '\u2666', 'USD': '\u2665', 'GBP': '\u2660'}
    unit_base = 100  # сколько копеек в рубле

    RUB = {'curency': 'Roubles', 'amount_nm': 'руб.', 'kopek_nm': 'коп.'}
    USD = {'curency': 'US dollar', 'amount_nm': 'dol.', 'kopek_nm': 'cent.'}
    GBP = {'curency': 'Great Britain Pound', 'amount_nm': 'Pound', 'kopek_nm': 'penny'}

    def __init__(self, amount, kopek, currency=RUB, sign=1):
        self.sign = sign
        self.amount = amount
        self.kopek = kopek
        self.currency = currency

    # приводит деньги к нормализованному представлению: 1 руб 120 коп --> 2 руб 20 коп
    #   -1 руб 10 коп = -110 коп
    #   -1 руб -10 коп = 100 + (-10) коп = 90 коп
    #   1 руб 110 коп = 2 руб 10 коп
    #   1 руб -110 коп = -10 коп

    def __str__(self):
        if self.sign == -1:
            _sign = '-'
        else:
            _sign = ''
        return f"{_sign}{str(self.amount)} {self.currency['amount_nm']} {str(self.kopek)} {self.currency['kopek_nm']}"

    def normolize(self):
        _amt = self.amount * self.unit_base + sign(self.amount) * self.kopek
        self.sign = sign(_amt)
        self.amount = abs(_amt) // self.unit_base
        self.kopek = abs(_amt) % self.unit_base

    def __add__(self, other_money):
        if self.currency != other_money.currency:
            print("Oops!  That was no valid number.  Try again...")
        else:
            _amt = (self.sign * (self.amount * self.unit_base + self.kopek)
                    + (other_money.sign * (other_money.amount * other_money.unit_base + other_money.kopek)))
            new_money = Money(sign=1, amount=0, kopek=_amt, currency=self.currency)
            new_money.normolize()
        return new_money

    def __sub__(self, other_money):
        if self.currency != other_money.currency:
            print("Oops!  That was no valid number.  Try again...")
        else:
            _amt = (self.sign * (self.amount * self.unit_base + self.kopek)
                    - (other_money.sign * (other_money.amount * other_money.unit_base + other_money.kopek)))
            new_money = Money(sign=1, amount=0, kopek=_amt, currency=self.currency)
            new_money.normolize()
        return new_money

    def __mul__(self, multiplier):
        __new_money = Money(amount=self.amount * multiplier, kopek=self.kopek * multiplier, currency=self.currency,
                            sign=self.sign)
        __new_money.normolize()
        return __new_money

    # сравнение (больше, меньше, равно, не равно)
    def __eq__(self, other_money):
        return (self.currency == other_money.currency and self.amount == other_money.amount
                and self.kopek == other_money.kopek and self.sign == other_money.kopek)

    def __gt__(self, other_money):
        return self.sign * (self.amount * self.unit_base + self.kopek) \
               > other_money.sign * (other_money.amount * other_money.unit_base + other_money.kopek)

    def __ge__(self, other_money):
        return self.sign * (self.amount * self.unit_base + self.kopek) \
               >= other_money.sign * (other_money.amount * other_money.unit_base + other_money.kopek)

    def __lt__(self, other_money):
        return self.sign * (self.amount * self.unit_base + self.kopek) \
               < other_money.sign * (other_money.amount * other_money.unit_base + other_money.kopek)

    def __le__(self, other_money):
        return self.sign * (self.amount * self.unit_base + self.kopek) \
               <= other_money.sign * (other_money.amount * other_money.unit_base + other_money.kopek)

    def __mod__(self, _percent):
        _amt = round(self.sign * (self.amount * self.unit_base + self.kopek) * _percent / 100, 0)
        __new_money = Money(amount=0
                            , kopek=_amt
                            , currency=self.currency
                            , sign=self.sign)
        __new_money.normolize()
        return __new_money

    def convert(self, to_currency):
        raise Exception("В разработке")
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)

        print(data_dict)


    # %%%
    # def __mod__(self, other_money):
    #     __new_money = Money(amount=0, kopek=abs(self.amount * self.unit_base + self.kopek) % abs(
    #         other_money.amount * other_money.unit_base + other_money.kopek) * self.sign() * other_money.sign())
    #     __new_money.normolize()
    #     return __new_money
    #
    # def __floordiv__(self, other_money):
    #     __new_money = Money(0, (self.amount * self.unit_base + self.kopek) // (
    #                 other_money.amount * other_money.unit_base + other_money.kopek))
    #     __new_money.normolize()
    #     return __new_money


################################################################################################################
money_sum1 = Money(amount=-10, kopek=60)
money_sum2 = Money(amount=-15, kopek=00)
money_sum3 = Money(amount=0, kopek=-60)
money_sum3.normolize()
print(money_sum3)

# приведение суммы к нормальному виду
money_sum1.normolize()
print(f'приведение суммы к нормальному виду: {money_sum1}')

# сложение
print(f'Пример сложения сумм: {money_sum1} + {money_sum2} = {money_sum1 + money_sum2}.')
print(f'Пример вычитания сумм: {money_sum1} - {money_sum2} = {money_sum1 - money_sum2}.')

# умножение на целое число
n = 10
print(f'Пример умножения на целое число: {money_sum1} * {n} = {money_sum1 * n}.')

# сравнение (больше, меньше, равно, не равно)
print(f'Cравнение (больше, меньше, равно, не равно)')
print(f' : {money_sum1} == {money_sum2} = {money_sum1 == money_sum2}.')
print(f' : {money_sum1} > {money_sum2} = {money_sum1 > money_sum2}.')
print(f' : {money_sum1} >= {money_sum2} = {money_sum1 >= money_sum2}.')
print(f' : {money_sum1} < {money_sum2} = {money_sum1 < money_sum2}.')
print(f' : {money_sum1} <= {money_sum2} = {money_sum1 <= money_sum2}.')

percent = 50
print(f' : {money_sum1} * {50}% = {money_sum1 % percent}.')

print(f' Конвертация: {money_sum1} в доллары == {money_sum1.convert(to_currency="USD")}.')


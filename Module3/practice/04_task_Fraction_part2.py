# Задание "Простые дроби"
# Задание "Простые дроби"
import math


class Fraction:
    def __init__(self, raw_fraction: str):  # Дробь в конструктор передается в виде строки
        fraction_parts = Fraction.parse_fraction(raw_fraction)
        self.numerator = (fraction_parts["whole"] * fraction_parts["denominator"]) + fraction_parts["numerator"]
        if fraction_parts["sign"] == -1:
            self.numerator *= -1
        self.denominator = fraction_parts["denominator"]
        self.simplificator()


    def simplificator(self):
        gsd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gsd
        self.denominator //= gsd

    @staticmethod
    def parse_fraction(raw_fraction):
            sign = 1
            if raw_fraction.startswith("-"):
                sign = -1
                raw_fraction = raw_fraction[1:]
            pair = raw_fraction.split()
            whole = 0
            if len(pair) == 2:
                whole = int(pair[0])
                raw_fraction = pair[-1]
            pair = raw_fraction.split('/')
            numerator = int(pair[0])
            denominator = int(pair[1])
            return {"sign": sign, "whole": whole, "numerator": numerator, "denominator": denominator}


    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: "-3 5/7"
        """
        whole = abs(self.numerator // self.denominator)
        numerator = self.numerator
        denominator = self.denominator
        if whole:
            numerator = abs(self.numerator % self.denominator)
        sign =''
        if self.numerator < 0:
            sign = '-'
        return f'{sign}{whole or ""}  {numerator}/{denominator}'

    def __add__(self, other):
        if self.denominator == other.denominator:
            self.numerator = self.numerator+other.numerator
        else:
            all_denominator = abs(self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
            self.numerator = self.numerator * (all_denominator/self.denominator) + other.numerator * (all_denominator/other.denominator)
        return 



    def __sub__(self, other):
        if self.denominator == other.denominator:
            self.numerator = self.numerator - other.numerator
        else:
            all_denominator = abs(self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
            self.numerator = self.numerator * (all_denominator / self.denominator) - other.numerator * (all_denominator / other.denominator)


    def __mul__(self, other):
        return




f1 = Fraction("3 12/15")
f2 = Fraction("-1 11/6")
f3 = Fraction("2/4")
f4 = Fraction("-3/4")

# TODO: Задание: реализуйте операции с дробями
# Сложение
f_sum = f1 + f2
print(f"{f1} + {f2} = {f_sum}")
# Вычитание
f_sub = f3 - f4
print(f"{f3} + {f4} = {f_sub}")
# Умножение
f_mult = f3 * f4
print(f"{f3} * {f4} = {f_mult}")

print(f1.denominator)
print(f2.denominator)

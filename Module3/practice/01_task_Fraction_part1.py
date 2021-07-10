# Задание "Простые дроби"
import math


class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        tokens = fraction_str.split(" ")
        if len(tokens) == 2:
            val = tokens[1].split('/')
            self.numerator = int(tokens[0]) * int(val[0])
            self.denominator = int(val[1])
        else:
            val = tokens[0].split('/')
            self.numerator = int(val[0])
            self.denominator = int(val[1])

    def __str__(self):
        sign = 1
        num = self.numerator
        if self.numerator < 0:
            sign = -1
            num = abs(self.numerator)
        integer = num // self.denominator
        numerator = num - integer * self.denominator
        gcd = math.gcd(numerator, self.denominator)
        numerator /= gcd
        denominator = self.denominator / gcd
        return self.__print_fraction([sign, integer, int(numerator), int(denominator)])

    def __print_fraction(self, fraction):
        sign = ""
        if fraction[0] == -1:
            sign = "-"
        if fraction[1] == 0 and fraction[2] == 0:
            return "0"
        elif fraction[1] == 0:
            return f"{sign}{fraction[2]}/{fraction[3]}"
        elif fraction[2] == 0:
            return f"{sign}{fraction[1]}"
        else:
            return f"{sign}{fraction[1]} {fraction[2]}/{fraction[3]}"

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(f"{n}/{d}")

    def __radd__(self, other):
        n = self.numerator + other * self.denominator
        d = self.denominator
        return Fraction(f"{n}/{d}")

    def __lt__(self, other):
        n1 = self.numerator * other.denominator
        n2 = other.numerator * self.denominator
        return n1 < n2

    def __gt__(self, other):
        n1 = self.numerator * other.denominator
        n2 = other.numerator * self.denominator
        return n1 > n2

    def __ge__(self, other):
        n1 = self.numerator * other.denominator
        n2 = other.numerator * self.denominator
        return n1 >= n2

    def __ne__(self, other):
        n1 = self.numerator * other.denominator
        n2 = other.numerator * self.denominator
        return n1 != n2

    def __eq__(self, other):
        n1 = self.numerator * other.denominator
        n2 = other.numerator * self.denominator
        return n1 == n2

    def __le__(self, other):
        n1 = self.numerator * other.denominator
        n2 = other.numerator * self.denominator
        return n1 <= n2

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(f"{n}/{d}")

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(f"{n}/{d}")


# Примеры создания дробей:
f1 = Fraction("-3 12/15")
print(f1)
f2 = Fraction("-1 2/6")
print(f2)
f3 = Fraction("2/4")
print(f3)
f4 = Fraction("-2/4")
print(f4)
f5 = Fraction("3/4")
print(f5)

# Сложение
f_sum = f1 + f2
print(f"{f1} + {f2} = {f_sum}")
# Вычитание
f_sub = f3 - f4
print(f"{f3} - {f4} = {f_sub}")
# Умножение
f_mult = f3 * f4
print(f"{f3} * {f4} = {f_mult}")
# Сравнение (> < == != <= >=)
if f5 > f4:
    print(f"{f5} > {f4}")
elif f5 < f4:
    print(f"{f5} < {f4}")
else:
    print(f"{f5} = {f4}")
# Сложение с целым(int) числом
f_sum2 = f1 + 2
print(f"{f1} + {2} = {f_sum2}")
f_sum3 = 2 + f1
print(f"{2} + {f1} = {f_sum2}")

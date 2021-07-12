# Задание "Простые дроби"
import math


class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        tokens = fraction_str.split(" ")
        val = tokens[-1].split('/')
        if len(tokens) == 2:  # есть и целая, и дробь
            sign = -1 if int(tokens[0]) < 0 else 1
            self.numerator = sign * (abs(int(tokens[0])) * int(val[1]) + int(val[0]))
            self.denominator = int(val[1])
        elif len(val) == 2:  # есть только дробь
            self.numerator = int(val[0])
            self.denominator = int(val[1])
        else:  # есть только целая
            self.numerator = int(val[0])
            self.denominator = 1
        # сокращаем дробь
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)

    def __str__(self):
        sign = -1 if self.numerator < 0 else 1
        integer = abs(self.numerator) // self.denominator
        numerator = abs(self.numerator) - integer * self.denominator
        return self.__print_fraction([sign, integer, int(numerator), self.denominator])

    @staticmethod
    def __print_fraction(fraction):
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

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(f"{n}/{d}")

    def __rsub__(self, other):
        n = self.denominator * other - self.numerator
        d = self.denominator
        return Fraction(f"{n}/{d}")

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(f"{n}/{d}")

    def __rmul__(self, other):
        n = self.numerator * other
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

    def __neg__(self):
        return Fraction(f"{-1 * self.numerator}/{self.denominator}")


expr = 5 + (Fraction("-2/3") - Fraction("-2") + Fraction("3/5") + Fraction("1 1/15")) * Fraction("-4 6/7") - -Fraction("4/7")
print(expr)

# Задание "Простые дроби"

import math

class Fraction:
    def __init__(self, raw_fraction):  # Дробь в конструктор передается в виде строки
        self.__sign = 1
        if raw_fraction.startswith("-"):
            self.__sign = -1
            raw_fraction = raw_fraction[1:]
        pair = raw_fraction.split()
        self.__whole = 0
        if len(pair) == 2:
            self.__whole = int(pair[0])
            raw_fraction = pair[-1]
        pair = raw_fraction.split('/')
        self.__numerator = int(pair[0])  # private
        self.__denominator = int(pair[1])
        # Упрощаем дробь:
        self.__simplificator()
        # неправильная дробь одним движением
        self.__inc_fraction_numerator = self.__sign * (self.__whole * self.__denominator + self.__numerator)

    def __simplificator(self): # private
        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd
        new_whole = 0
        if self.__numerator > self.__denominator:
            new_whole = self.__numerator // self.__denominator
            self.__numerator = self.__numerator % self.__denominator

        self.__whole = self.__whole + new_whole

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: "-3 5/7"
        """
        whole = self.__whole * self.__sign
        if whole:
            return f"{whole} {self.__numerator}/{self.__denominator}"
        else:
            numerator = self.__numerator * self.__sign
            return f"{numerator}/{self.__denominator}"

    def __add__(self,other_fraction:'Fraction'):
        devider = math.lcm(self.__denominator, other_fraction.__denominator)
        common_numerator = self.__inc_fraction_numerator * ((devider / self.__denominator)) + other_fraction.__inc_fraction_numerator  * ((devider / other_fraction.__denominator))
        return Fraction(f"{int(common_numerator)}/{devider}")

    def __sub__(self, other_fraction:'Fraction'):
        devider = math.lcm(self.__denominator, other_fraction.__denominator)
        common_numerator = self.__inc_fraction_numerator * ((devider / self.__denominator)) - other_fraction.__inc_fraction_numerator * ((devider / other_fraction.__denominator))
        return Fraction(f"{int(common_numerator)}/{devider}")


    def __mul__(self,other_fraction:'Fraction'):
        common_numerator = self.__inc_fraction_numerator * other_fraction.__inc_fraction_numerator
        common_denominator = self.__denominator * other_fraction.__denominator
        return Fraction(f"{int(common_numerator)}/{common_denominator}")





f1 = Fraction("3 12/15")
f2 = Fraction("-1 11/6")
f3 = Fraction("2/4")
f4 = Fraction("-3/4")

# TODO: Задание: реализуйте операции с дробями
# Сложение
f_sum = f1 + f2
print(f"{f1} + {f2} = {f_sum}")

f_sum2 = f3 + f4
print(f"{f3} + {f4} = {f_sum2}")
# Вычитание
f_sub = f3 - f4
print(f"{f3} - {f4} = {f_sub}")
# Умножение
f_mult = f3 * f4
print(f"{f3} * {f4} = {f_mult}")

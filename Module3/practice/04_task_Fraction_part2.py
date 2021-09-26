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

    def __simplificator(self):  # private
        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd
        new_whole = 0
        if self.__numerator > self.__denominator:
            new_whole = self.__numerator // self.__denominator
            self.__numerator = self.__numerator % self.__denominator

        self.__whole = self.__whole + new_whole

    def __lcm(self, other_fraction): #Приводим к общему знаменателю
        lcm = abs(self.__denominator * other_fraction.__denominator) // math.gcd(self.__denominator,
                                                                                 other_fraction.__denominator)
        mult_self = lcm // self.__denominator
        mult_other = lcm // other_fraction.__denominator
        return lcm, mult_self, mult_other

    def __add__(self, other_fraction: 'Fraction'):
        denominator = self.__lcm(other_fraction)[0]
        mult_self = self.__lcm(other_fraction)[1]
        mult_other = self.__lcm(other_fraction)[2]
        numerator_self = (self.__numerator * mult_self + self.__whole * denominator) \
                         * self.__sign
        numerator_other = (other_fraction.__numerator * mult_other + other_fraction.__whole * denominator) \
                          * other_fraction.__sign
        total_numerator = numerator_self + numerator_other
        return Fraction(f"{total_numerator}/{denominator}")

    def __sub__(self, other_fraction: 'Fraction'):
        denominator = self.__lcm(other_fraction)[0]
        mult_self = self.__lcm(other_fraction)[1]
        mult_other = self.__lcm(other_fraction)[2]
        numerator_self = (self.__numerator * mult_self + self.__whole * denominator) \
                         * self.__sign
        numerator_other = (other_fraction.__numerator * mult_other + other_fraction.__whole * denominator) \
                          * other_fraction.__sign
        total_numerator = numerator_self - numerator_other
        return Fraction(f"{total_numerator}/{denominator}")

    def __mul__(self, other_fraction: 'Fraction'):
        numerator_self = (self.__whole * self.__denominator + self.__numerator) * self.__sign
        numerator_other = (other_fraction.__whole * other_fraction.__denominator + other_fraction.__numerator) * other_fraction.__sign
        total_numerator = numerator_self * numerator_other
        total_denominator = self.__denominator * other_fraction.__denominator
        return Fraction(f"{total_numerator}/{total_denominator}")

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        """
        if self.__whole:
            return f"{self.__sign * self.__whole} {self.__numerator}/{self.__denominator}"
        else:
            return f"{self.__sign * self.__numerator}/{self.__denominator}"

f1 = Fraction("4 4/12") # 52/12
f2 = Fraction("-2 7/8") # -23/8
f3 = Fraction("2/4")
f4 = Fraction("3/4")

# TODO: Задание: реализуйте операции с дробями
# Сложение
f_sum = f1 + f2 # 8/24 - 21/24 = 29/24 = -13/24
# 8 + -21
print(f"{f1} + {f2} = {f_sum}") # ...
f_sum1 = f_sum + f3
print(f"{f_sum} + {f3} = {f_sum1}")
# Вычитание
f_sub = f3 - f4
print(f"{f3} - {f4} = {f_sub}")
f_sub1 = f_sum - f3
print(f"{f_sum} - {f3} = {f_sub1}")
# # Умножение
f_mult = f3 * f4
print(f"{f3} * {f4} = {f_mult}")
f_mult2 = f_sub1 * f4
print(f"{f_sub1} * {f4} = {f_mult2}")

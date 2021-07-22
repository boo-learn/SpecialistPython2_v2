# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        pair = fraction_str.split(" ")
        if len(pair) == 2:
            whole = int(pair[0])
        else:
            whole = 0

        pair = pair[-1].split("/")
        num = int(pair[0])
        den = int(pair[1])

        num += abs(whole) * den
        if whole < 0:
            num = -num
        self.numerator = num
        self.denominator = den  # знаменатель
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: -3 5/7
        """
        whole = abs(self.numerator) // self.denominator
        new_numerator = abs(self.numerator) % self.denominator
        if self.numerator < 0 and whole:
            whole = -whole
        elif self.numerator < 0:
            new_numerator = -new_numerator
        return f"{whole if whole else ''} {new_numerator}/{self.denominator}"

    def __add__(self, other):
    	numerator_now = (self.denominator * other.numerator) + (other.denominator * self.numerator)
    	denomerator_now = self.denominator * other.denominator
    	return Fraction(f'{numerator_now}/{denomerator_now}')

# Примеры создания дробей:
f1 = Fraction("3 12/15")
f2 = Fraction("-1 2/6")
f3 = Fraction("2/4")
f4 = Fraction("-2/4")
f5 = Fraction("3/4")
print(f1)
print(f2)
print(f3)
print(f4)
# TODO: Задание: реализуйте операции с дробями
# Примечание: в начальной реализации получившиеся дроби упрощать не требуется.
# При операциях с дробями их можно приводить к максимальному общему знаменателю.

# Сложение
f_sum = f1 + f2
print(f"{f1} + {f2} = {f_sum}")
# # Вычитание
# f_sub = f3 - f4
# print(f"{f3} + {f4} = {f_sub}")
# # Умножение
# f_mult = f3 * f4
# print(f"{f3} * {f4} = {f_mult}")
# # Сравнение (> < == != <= >=)
# if f5 > f4:
#     print(f"{f5} > {f4}")
# elif f5 < f4:
#     print(f"{f5} < {f4}")
# else:
#     print(f"{f5} = {f4}")
# # Сложение с целым(int) числом
# f_sum2 = f1 + 2
# print(f"{f1} + {2} = {f_sum2}")
# f_sum3 = 2 + f1
# print(f"{2} + {f1} = {f_sum2}")

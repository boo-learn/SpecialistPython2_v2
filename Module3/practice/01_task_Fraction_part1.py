# Задание "Простые дроби"

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
        return f"{self.numerator}/{self.denominator}"


# Примеры создания дробей:
f1 = Fraction("3 12/15")
print(f1)
f2 = Fraction("-1 2/6")
print(f2)
f3 = Fraction("2/4")
print(f3)
f4 = Fraction("-2/4")
print(f4)
f5 = Fraction("3/4")
print(f5)

# TODO: Задание: реализуйте операции с дробями
# Примечание: в начальной реализации получившиеся дроби упрощать не требуется.
# При операциях с дробями их можно приводить к максимальному общему знаменателю.

# Сложение
# f_sum = f1 + f2
# print(f"{f1} + {f2} = {f_sum}")
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

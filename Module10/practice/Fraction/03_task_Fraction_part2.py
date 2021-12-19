# Задание "Простые дроби"

class Fraction:
    def __init__(self, raw_fraction):
        ...
    # TODO: сюда копируем класс Дроби из предыдущей задачи


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


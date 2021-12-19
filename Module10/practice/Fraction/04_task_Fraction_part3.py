# Задание "Простые дроби"

class Fraction:
    def __init__(self, raw_fraction):
        ...
    # TODO: сюда копируем класс Дроби из предыдущей задачи


f1 = Fraction("3 12/15")
f2 = Fraction("-1 11/6")

# TODO: Задание: реализуйте операции с дробями
# Сравнение (> < ==)
if f1 > f2:
    print(f"{f1} > {f2}")
elif f1 < f2:
    print(f"{f1} < {f2}")
else:
    print(f"{f1} = {f2}")


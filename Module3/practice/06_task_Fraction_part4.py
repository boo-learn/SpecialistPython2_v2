# Задание "Простые дроби"

class Fraction:
    pass
    # TODO: сюда копируем класс Дроби из предыдущей задачи


f1 = Fraction("3 12/15")
f2 = Fraction("-1 11/6")
f3 = Fraction("2/4")
f4 = Fraction("-3/4")

# TODO: Задание: реализуйте cложение дроби с целым(int) числом
f_sum2 = f1 + 2
print(f"{f1} + {2} = {f_sum2}")
f_sum3 = 2 + f1
print(f"{2} + {f1} = {f_sum2}")


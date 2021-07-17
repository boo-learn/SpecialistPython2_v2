# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        pair = fraction_str.split()
        if len(pair) == 2:
            hole = int(pair[0])
        else:
            hole = 0
        f = pair[-1]
        numerator = int(f.split('/')[0])
        denominator = int(f.split('/')[1])
        self.numerator = hole * denominator + numerator * (-1 if hole < 0 else 1)  # числитель, в скобках перенос знака
        self.denominator = denominator  # знаменатель
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: -3 5/7
        """
        if int(self.numerator) == 0:
            return f'{self.numerator}'
        # упрощение дроби - начало
        num = abs(self.numerator)
        denom = abs(self.denominator)
        while True:
            if num > denom:
                num -= denom
            elif num < denom:
                denom -= num
            elif num == denom:
                break
        numerator = int(self.numerator / num)  # числитель неправильной дроби
        denominator = int(self.denominator / denom)  # знаменатель
        # упрощение дроби - конец
        integer_part = int(numerator / denominator)  # целая часть смешанной дроби
        numerator = (int(numerator - integer_part * denominator))  # числитель смешанной дроби
        if numerator == 0:
            return f'{integer_part}'
        elif integer_part == 0:
            return f'{numerator}/{denominator}'
        else:
            return f'{integer_part} {abs(numerator)}/{denominator}'

    def __add__(self, other_f):
        if self.denominator != other_f.denominator:
            new_denominator = self.denominator * other_f.denominator
            new_numerator = self.numerator * other_f.denominator + self.denominator * other_f.numerator
        else:
            new_denominator = self.denominator
            new_numerator = self.numerator + other_f.numerator
        return Fraction(f'{new_numerator}/{new_denominator}')

    def __sub__(self, other_f):
        if self.denominator != other_f.denominator:
            new_denominator = self.denominator * other_f.denominator
            new_numerator = self.numerator * other_f.denominator - self.denominator * other_f.numerator
        else:
            new_denominator = self.denominator
            new_numerator = self.numerator - other_f.numerator
        return Fraction(f'{new_numerator}/{new_denominator}')

    def __mul__(self, other_f):
        new_denominator = self.denominator * other_f.denominator
        new_numerator = self.numerator * other_f.numerator
        return Fraction(f'{new_numerator}/{new_denominator}')

    def __gt__(self, other_f):
        return self.numerator * other_f.denominator > self.denominator * other_f.numerator

    def __lt__(self, other_f):
        return self.numerator * other_f.denominator < self.denominator * other_f.numerator

    def __eq__(self, other_f):
        return self.numerator * other_f.denominator == self.denominator * other_f.numerator

    def __radd__(self, other_f):
        if self.denominator != other_f.denominator:
            new_denominator = self.denominator * other_f.denominator
            new_numerator = self.numerator * other_f.denominator + self.denominator * other_f.numerator
        else:
            new_denominator = self.denominator
            new_numerator = self.numerator + other_f.numerator
        return Fraction(f'{new_numerator}/{new_denominator}')

    def __rsub__(self, other_f):
        if self.denominator != other_f.denominator:
            new_denominator = self.denominator * other_f.denominator
            new_numerator = self.numerator * other_f.denominator - self.denominator * other_f.numerator
        else:
            new_denominator = self.denominator
            new_numerator = self.numerator - other_f.numerator
        return Fraction(f'{new_numerator}/{new_denominator}')

    def __rmul__(self, other_f):
        new_denominator = self.denominator * other_f.denominator
        new_numerator = self.numerator * other_f.numerator
        return Fraction(f'{new_numerator}/{new_denominator}')


# Примеры создания дробей:
f1 = Fraction("3 12/15")
f2 = Fraction("-1 2/6")
f3 = Fraction("2/4")
f4 = Fraction("-2/4")
f5 = Fraction("3/4")

# Примечание: в начальной реализации получившиеся дроби упрощать не требуется.
# При операциях с дробями их можно приводить к максимальному общему знаменателю.

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
print(f"{2} + {f1} = {f_sum3}")

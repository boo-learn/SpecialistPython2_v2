# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки

        # Поиск НОД
        def gcd(a, b):
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return a

        pair = fraction_str.split()
        whole = 0
        if len(pair) == 2:
            whole = int(pair[0])
            pair = pair[1:]
        fraction = pair[0].split('/')

        self.numerator = int(fraction[0])
        self.denominator = int(fraction[1])
        if whole >= 0:
            self.numerator += whole * self.denominator
        else:
            self.numerator += abs(whole) * self.denominator
            self.numerator *= -1

        nod = gcd(abs(self.numerator), self.denominator)
        self.numerator //= nod
        self.denominator //= nod

    def __repr__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: -3 5/7
        """

        if self.numerator >= 0:
            whole = self.numerator // self.denominator
            numerator = self.numerator - self.denominator * whole
        else:
            whole = abs(self.numerator) // self.denominator
            numerator = abs(self.numerator) - self.denominator * whole
            if whole:
                whole *= -1
            else:
                numerator *= -1
        # return f"{whole or ''} {numerator}/{self.denominator}"
        return f"{whole} {numerator}/{self.denominator}" if whole else f"{numerator}/{self.denominator}"

    def __add__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d // self.denominator)
        numerator2 = other_f.numerator * (common_d // other_f.denominator)
        common_n = numerator1 + numerator2
        return Fraction(f"{common_n}/{common_d}")

    def __radd__(self, other_f):
        return self.__add__(other_f)

    def __sub__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d // self.denominator)
        numerator2 = other_f.numerator * (common_d // other_f.denominator)
        common_n = numerator1 - numerator2
        return Fraction(f"{common_n}/{common_d}")

    def __mul__(self, other_f):
        common_n = self.numerator * other_f.numerator
        common_d = self.denominator * other_f.denominator
        return Fraction(f"{common_n}/{common_d}")

    def __gt__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d // self.denominator)
        numerator2 = other_f.numerator * (common_d // other_f.denominator)
        return numerator1 > numerator2

    def __lt__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d // self.denominator)
        numerator2 = other_f.numerator * (common_d // other_f.denominator)
        return numerator1 < numerator2

    def __eq__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d // self.denominator)
        numerator2 = other_f.numerator * (common_d // other_f.denominator)
        return numerator1 == numerator2

    def __ne__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d // self.denominator)
        numerator2 = other_f.numerator * (common_d // other_f.denominator)
        return numerator1 != numerator2


# Примеры создания дробей:
f1 = Fraction("-4/6")
f2 = Fraction("3 1/6")
f3 = Fraction("2/4")
f4 = Fraction("3/4")
f5 = Fraction("-1 2/10")
f6 = Fraction("-1 1/5")

# Сложение
f_sum = f1 + f2
print(f"{f1} + {f2} = {f_sum}")

# Вычитание
f_sub = f4 - f3
print(f"{f4} - {f3} = {f_sub}")

# Умножение
f_mult = f2 * f4
print(f"{f2} * {f4} = {f_mult}")

# Сравнение (> < == != <= >=)
print(f"{f5} > {f4}" if f5 > f4 else f"{f5} < {f4}")
print(f"{f3} > {f4}" if f3 < f4 else f"{f3} < {f4}")
print(f"{f5} = {f6}" if f5 == f6 else f"{f5} != {f6}")
print(f"{f5} != {f6}" if f5 != f6 else f"{f5} = {f6}")

# Сложение с целым(int) числом
f_sum2 = f1 + 3
print(f"{f1} + {3} = {f_sum2}")
f_sum3 = 2 + f1
print(f"{2} + {f1} = {f_sum3}")

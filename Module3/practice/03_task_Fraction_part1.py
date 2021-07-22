# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        pair = fraction_str.split(' ')
        if len(pair) == 2:
            whole = int(pair[0])
        else:
            whole = 0
        pair = pair[-1].split('/')
        num = int(pair[0])
        den = int(pair[1])

        num += abs(whole) * den
        if whole < 0:
            num = - num
        self.numerator = num
        self.denominator = den
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
            whole = - whole
        elif self.numerator < 0:
            new_numerator = - new_numerator
        return f'{whole if whole else ""} {new_numerator}/{self.denominator}'

    def __add__(self, other):
        if self.denominator == other.denominator:
            new_den = self.denominator
            new_nom = self.numerator + other.numerator
        else:
            new_nom = self.numerator * other.denominator + other.numerator * self.denominator
            new_den = self.denominator * other.denominator
        return Fraction(f'{new_nom}/{new_den}')

    def __sub__(self, other):
        if self.denominator == other.denominator:
            new_den = self.denominator
            new_nom = self.numerator - other.numerator
        else:
            new_nom = self.numerator * other.denominator - other.numerator * self.denominator
            new_den = self.denominator * other.denominator
        return Fraction(f'{new_nom}/{new_den}')

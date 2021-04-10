# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        import re
        rez = re.findall(r'.?\d*', fraction_str)
        if len(rez) == 3:
            self.numerator = int(rez[0])
            self.denominator = int(rez[1][1:])
        else:
            whole = int(rez[0])
            self.denominator = int(rez[2][1:])
            self.numerator = int(rez[1]) + abs(whole) * self.denominator
            if whole < 0:
                self.numerator = -self.numerator
        nod = self._nod_find(abs(self.numerator), self.denominator)
        self.numerator = self.numerator // nod
        self.denominator = self.denominator // nod

    def __repr__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: -3 5/7
        """
        if abs(self.numerator) < self.denominator:
            if self.numerator:
                out = f'{self.numerator}/{self.denominator}'
            else:
                out = '0'
        else:
            whole = abs(self.numerator) // self.denominator
            numerator = abs(self.numerator) - whole * self.denominator
            if self.numerator < 0:
                whole = - whole
            if numerator == 0:
                out = f'{whole}'
            else:
                out = f'{whole} {numerator}/{self.denominator}'
        return out

    def __add__(self, other):
        if type(other) == Fraction:
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
        elif type(other) == int:
            num = self.numerator + other * self.denominator
            den = self.denominator
        return Fraction(f'{num}/{den}')

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(f'{num}/{den}')

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(f'{num}/{den}')

    def __truediv__(self, other):
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(f'{num}/{den}')

    def __gt__(self, other):
        val_self = self.numerator * other.denominator
        val_other = other.numerator * self.denominator
        return val_self > val_other

    def __lt__(self, other):
        val_self = self.numerator * other.denominator
        val_other = other.numerator * self.denominator
        return val_self < val_other

    def __ge__(self, other):
        val_self = self.numerator * other.denominator
        val_other = other.numerator * self.denominator
        return val_self >= val_other

    def __le__(self, other):
        val_self = self.numerator * other.denominator
        val_other = other.numerator * self.denominator
        return val_self <= val_other

    def __eq__(self, other):
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __ne__(self, other):
        return (self.numerator != other.numerator) or (self.denominator != other.denominator)

    def _nod_find(self, num_1, num_2):
        while num_1 != 0 and num_2 != 0:
            if num_1 > num_2:
                num_1 = num_1 % num_2
            else:
                num_2 = num_2 % num_1

        return num_1 + num_2



# Задание на доработку класса
# Доработайте класс дробей так, чтобы при создании дроби, дробь упрощалась и сокращалась.
# Подсказка: Для сокращения дроби вам понадобится "Наибольший общий делитель",
# а для его поиска можете использовать алгоритм Эвклида(подробнее тут: https://younglinux.info/algorithm/euclidean).

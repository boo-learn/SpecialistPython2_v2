import math


class Fraction:
    def __init__(self, raw_fraction: str):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        self.sign = 1
        if raw_fraction.startswith("-"):
            self.sign = -1
            raw_fraction = raw_fraction[1:]
        pair = raw_fraction.split()
        self.whole = 0
        if len(pair) == 2:
            self.whole = int(pair[0])
            raw_fraction = pair[-1]
        pair = raw_fraction.split('/')
        self.numerator = int(pair[0])  # числителя
        self.denominator = int(pair[1])  # знаменателя

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: "-3 5/7"
        """
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd
        new_whole = 0
        if self.numerator > self.denominator:
            new_whole = self.numerator // self.denominator
            self.numerator = self.numerator % self.denominator

        whole = self.whole + new_whole
        whole = whole * self.sign
        if whole:
            return f'{whole} {self.numerator}/{self.denominator}'
        else:
            self.numerator = self.numerator * self.sign
            return f'{self.numerator}/{self.denominator}'


# Простые дроби заданы в виде строки

# Конструктор принимает простую дробь в виде строки формата: <Целая часть> <числитель>/<знаменатель>
# целая_часть может отсутствовать, числитель и знаменатель всегда присутствуют
# дроби могут быть отрицательными или положительными
f1 = Fraction("3 12/15")
f2 = Fraction("-1 11/6")
f3 = Fraction("2/4")
f4 = Fraction("-5/4")

# TODO: Задание: реализуйте class Fraction, который выводит дробь в упрощенном виде с выделением целой части
print(f1)  # 3 4/5
print(f2)  # -2 5/6
print(f3)  # 1/2
print(f4)  # -1 1/4

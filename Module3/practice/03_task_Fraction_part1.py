# Задание "Простые дроби"
import math


class Fraction:
    def __init__(self, raw_fraction):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        self.numerator = 0
        self.denominator = 0
        self.raw_fraction = raw_fraction

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: "-3 5/7"
        """
        import math

        def parse_fraction(raw_fraction: str):
            sign = 1
            if raw_fraction.startswith("-"):
                sign = -1
                raw_fraction = raw_fraction[1:]
            pair = raw_fraction.split()
            whole = 0
            if len(pair) == 2:
                whole = int(pair[0])
                raw_fraction = pair[-1]
            pair = raw_fraction.split('/')
            numerator = int(pair[0])
            denominator = int(pair[1])
            return {"sign": sign, "whole": whole, "numerator": numerator, "denominator": denominator}


        raw_fract = self.raw_fraction
        fraction_parts = parse_fraction(raw_fract)
        # 1.делаем преобразование в правильную дробь
        if fraction_parts['numerator'] > fraction_parts['denominator']:
            whole = fraction_parts['numerator'] // fraction_parts['denominator']
            fraction_parts['whole'] += whole
            numerator = fraction_parts['numerator'] % fraction_parts['denominator']
            fraction_parts['numerator'] = numerator
            # 2 упрощаем дробь
        gsd = math.gcd(fraction_parts['numerator'], fraction_parts['denominator'])
        fraction_parts['numerator'] //= gsd
        fraction_parts['denominator'] //= gsd
        sign = ""
        if fraction_parts['sign'] == -1:
            sign = '-'
        self.numerator = (fraction_parts["whole"] * fraction_parts["denominator"]) + fraction_parts["numerator"]
        self.denominator = fraction_parts["denominator"]

        return f'{sign}{fraction_parts["whole"] or ""}  {fraction_parts["numerator"]}/{fraction_parts["denominator"]}'




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

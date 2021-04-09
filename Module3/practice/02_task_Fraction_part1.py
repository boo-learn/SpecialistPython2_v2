# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        self.numerator, self.denominator = self.__parse_fraction_str(fraction_str)
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: -3 5/7
        """
        return self.to_str(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def to_str(self, numerator, denominator):
        if abs(numerator) > denominator:
            if numerator < 0:
                if numerator % denominator == 0:
                    left = f'-{abs(numerator // denominator)}'
                else:
                    left = f'-{abs(numerator // denominator) - 1}'
                left = left + f' {abs(numerator) % denominator}'
            else:
                left = f'{numerator // denominator} {numerator % denominator}'
        else:
            return f'{numerator}/{denominator}'
        right = f'/{denominator}'
        return left + right

    def __parse_fraction_str(self, s: str):
        s = s.split(' ')
        try:
            substring = s[1].split('/')
            denominator = int(substring[1])
            if int(s[0]) < 0:
                numerator = (abs(int(s[0])) * denominator + int(substring[0])) * -1
            else:
                numerator = int(s[0]) * denominator + int(substring[0])
        except IndexError:
            substring = s[0].split('/')
            denominator = int(substring[1])
            numerator = int(substring[0])
        return numerator, denominator

    def __add_sub_helper(self, other):
        if type(other) == int:
            other = Fraction(f'{other} 0/1')
        common_divisor = self.denominator * other.denominator
        left_operand = self.numerator * (int(common_divisor / self.denominator))
        right_operand = other.numerator * (int(common_divisor / other.denominator))
        return common_divisor, left_operand, right_operand

    def __add__(self, other):
        common_divisor, left_operand, right_operand = self.__add_sub_helper(other)
        res_numerator = left_operand + right_operand
        return Fraction(self.to_str(res_numerator, common_divisor))

    def __sub__(self, other):
        common_divisor, left_operand, right_operand = self.__add_sub_helper(other)
        res_numerator = left_operand - right_operand
        return Fraction(self.to_str(res_numerator, common_divisor))

    def __mul__(self, other):
        return Fraction(self.to_str(
            numerator=self.numerator * other.numerator,
            denominator=self.denominator * other.denominator
        ))

    def __gt__(self, other):
        _, left_operand, right_operand = self.__add_sub_helper(other)
        return left_operand > right_operand

    def __ge__(self, other):
        _, left_operand, right_operand = self.__add_sub_helper(other)
        return left_operand >= right_operand

    def __lt__(self, other):
        _, left_operand, right_operand = self.__add_sub_helper(other)
        return left_operand < right_operand

    def __le__(self, other):
        _, left_operand, right_operand = self.__add_sub_helper(other)
        return left_operand <= right_operand
    
    def __ne__(self, other):
        _, left_operand, right_operand = self.__add_sub_helper(other)
        return left_operand != right_operand
    
    def __eq__(self, other):
        _, left_operand, right_operand = self.__add_sub_helper(other)
        return left_operand == right_operand
    

if __name__ == '__main__':
    # Примеры создания дробей:
    f1 = Fraction("3 12/15")
    f2 = Fraction("-1 2/6")
    f3 = Fraction("2/4")
    f4 = Fraction("-2/4")
    f5 = Fraction("3/4")
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)

    # TODO: Задание: реализуйте операции с дробями
    # Примечание: в начальной реализации получившиеся дроби упрощать не требуется.
    # При операциях с дробями их можно приводить к максимальному общему знаменателю.

    # # Сложение
    f_sum = f1 + f2
    print('sum')
    print(f"{f1} + {f2} = {f_sum}")
    # # Вычитание
    f_sub = f3 - f4
    print(f"{f3} - {f4} = {f_sub}")
    # # Умножение
    f_mult = f3 * f4
    print(f"{f3} * {f4} = {f_mult}")
    # # Сравнение (> < == != <= >=)
    if f5 > f4:
        print(f"{f5} > {f4}")
    elif f5 < f4:
        print(f"{f5} < {f4}")
    else:
        print(f"{f5} = {f4}")
    # # Сложение с целым(int) числом
    f_sum2 = f1 + 2
    print(f"{f1} + {2} = {f_sum2}")
    # f_sum3 = 2 + f1
    # print(f"{2} + {f1} = {f_sum2}")

# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        self.numerator = ...  # числителя
        self.denominator = ...  # знаменатель
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе

        symb = fraction_str.split(" ")
        if len(symb) == 2:
            value = symb[1].split('/')
            self.numerator = int(symb[0]) * int(value[0])
            self.denominator = int(value[1])
        else:
            value = symb[0].split('/')
            self.numerator = int(value[0])
            self.denominator = int(value[1])

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: -3 5/7
        """
        return f"{self.numerator}/{self.denominator}"


# Примеры создания дробей:
f1 = Fraction("3 12/15")
print(f1)
f2 = Fraction("-1 2/6")
print(f2)
f3 = Fraction("2/4")
print(f3)
f4 = Fraction("-2/4")
print(f4)
f5 = Fraction("3/4")
print(f5)

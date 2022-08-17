# Задание:
# Напишите класс для работы с римскими цифрами.
# Подробнее про Римские цифры тут: http://graecolatini.bsu.by/htm-different/num-converter-roman.htm
SYMBOLS = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}


class Roman:
    def __init__(self, number):
        self.number = number

    def get_roman(self):
        roman_number = ''
        number = self.number
        for key, value in SYMBOLS.items():
            roman_number += number // key * value
            number = number % key
        return roman_number

    def __str__(self):
        return self.get_roman()

    def __add__(self, other):
        return Roman(self.number + other.number)

    def __mul__(self, other):
        return Roman(self.number * other)

# Реализуйте операции:
# Сложение
# Вычитание
# Умножение
# Целочисленное деление
# Сравнение (> < == !=)
# Пример:
n1 = Roman(10)
n2 = Roman(14)
print(n1)  # X
print(n2)  # XIV
n3 = n1 + n2
print(n3)  # XXIV
n3 *= 2
print(n3)  # XLVIII

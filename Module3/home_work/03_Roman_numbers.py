class Roman:
    digits_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                   6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):

        return self.to_roman()

    def __add__(self, other_amount):

        return Roman(self.amount + other_amount.amount)

    def __sub__(self, other_amount):

        return Roman(self.amount - other_amount.amount)

    def __mul__(self, x: int):

        return Roman(self.amount * x)

    def __floordiv__(self, other_amount):

        return Roman(self.amount // other_amount.amount)

    def __eq__(self, other_amount):

        return self.amount == other_amount.amount

    def __gt__(self, other_amount):

        return self.amount > other_amount.amount

    def __lt__(self, other_amount):

        return self.amount < other_amount.amount

    def __ge__(self, other_amount):

        return self.amount >= other_amount.amount

    def __le__ (self, other_amount):

        return self.amount <= other_amount.amount

    def to_roman(self):

        self.thousands = self.amount // 1000
        self.remainder_from_thousands = self.amount % 1000
        self.five_hundreds = self.remainder_from_thousands // 500
        self.remainder_from_five_hundreds = self.remainder_from_thousands % 500
        self.hundreds = self.remainder_from_five_hundreds // 100
        self.remainder_from_hundreds = self.remainder_from_five_hundreds % 100
        self.fifties = self.remainder_from_hundreds // 50
        self.remainder_from_fifties = self.remainder_from_hundreds % 50
        self.tens = self.remainder_from_fifties // 10
        self.remainder_from_tens = self.remainder_from_fifties % 10

        self.roman = ''

        self.roman += 'M' * self.thousands

        if self.remainder_from_thousands // 100 == 9:
            self.roman += 'CM'
        elif self.five_hundreds:
            self.roman += 'D'

        if self.remainder_from_thousands // 100 == 9:
            self.roman = self.roman
        elif self.hundreds == 4:
            self.roman += 'CD'
        else:
            self.roman += 'C' * self.hundreds

        if self.fifties == 4:
            self.roman += 'XC'
        elif self.fifties:
            self.roman += 'L'

        if self.tens == 4:
            self.roman += 'XL'
        elif self.tens:
            self.roman += 'X' * self.tens

        if self.remainder_from_tens:
            self.roman += Roman.digits_dict[self.remainder_from_tens]

        return self.roman

    def to_arabic(self):

        return self.amount

# ТЕСТИРОВАНИЕ

# Создаем два объекта
roman1 = Roman(2022)
roman2 = Roman(492)

# Тестируем строковое представление
print("Тестируем строкое представление")
print(f'{roman1.to_arabic()} -> {roman1}')
print(f'{roman2.to_arabic()} -> {roman2}')

# Складываем
print('Складываем')
total = roman1 + roman2
print(total)

# У любого числа можно вернуть арабское значение через метод to_arabic()
print('У любого числа можно вернуть арабское значение через метод to_arabic()')
print(f'{total} -> {total.to_arabic()}')

# Вычитаем без дополнительной переменной
print('Вычитаем без дополнительной переменной')
print(roman1 - roman2)

# Умножаем
print('Умножаем')
print(roman2 * 3)

# сравнения
print(f'{roman1} больше {roman2}? -> {roman1 > roman2}')
print(f'{roman1} меньше {roman2}? -> {roman1 < roman2}')
print(f'{roman1} равно {roman1}? -> {roman1 == roman1}')
print(f'{roman1} меньше или равно {roman2}? -> {roman1 >= roman2}')
print(f'{roman2} больше или равно {roman1}? -> {roman1 <= roman2}')

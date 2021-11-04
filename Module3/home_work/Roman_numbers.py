class Roman:
    def __init__(self, number):
        self.roman_number = number
        self.convert_numbers()

    def __add__(self, other_number):  # сложение
        return Roman(self.roman_number + other_number.roman_number)

    def __sub__(self, other_number):  # вычитание
        return Roman(self.roman_number - other_number.roman_number)

    def __mul__(self, other_number):  # умножение
        return Roman(self.roman_number * other_number.roman_number)

    def __gt__(self, other_number):  # сравнение >
        if True:
            return Roman(self.roman_number > other_number.roman_number)

    def __lt__(self, other_number):  # сравнение <
        if True:
            return Roman(self.roman_number < other_number.roman_number)

    def __le__(self, other_number):  # сравнение меньше или равно <=
        if True:
            return Roman(self.roman_number <= other_number.roman_number)

    def __ge__(self, other_number):  # сравнение меньше или равно >=
        if True:
            return Roman(self.roman_number >= other_number.roman_number)

    def __eq__(self, other_number):  # сравнение ==
        if True:
            return Roman(self.roman_number == other_number.roman_number)

    def __ne__(self, other_number):  # сравнение !=
        if True:
            return Roman(self.roman_number != other_number.roman_number)

    def convert_numbers(self):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[self // 1000]
        h = hunds[self // 100 % 10]
        te = tens[self // 10 % 10]
        o = ones[self % 10]

        return t + h + te + o

    def __str__(self):
        return f'{self.roman_number}'


number = Roman(30)
number2 = Roman(40)
print(number)
print(number2)
print(number < number2)

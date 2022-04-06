import copy


class Roman:
    def __init__(self, number):
        self.dec_number = number
        self.roman_number = ''
        self.roman_number += self.dec_number // 1000 * 'M'
        min_number = self.dec_number % 1000
        if min_number >= 900:
            self.roman_number += 'CM'
            min_number -= 900
        elif min_number >= 500:
            self.roman_number += 'D'
            min_number -= 500
        elif min_number >= 400:
            self.roman_number += 'CD'
            min_number -= 400
        else:
            self.roman_number += min_number // 100 * 'C'
        min_number %= 100
        if min_number >= 90:
            self.roman_number += 'XC'
            min_number -= 90
        elif min_number >= 50:
            self.roman_number += 'L'
            min_number -= 50
        elif min_number >= 40:
            self.roman_number += 'XL'
            min_number -= 40
        else:
            self.roman_number += min_number // 10 * 'X'
        min_number %= 10
        if min_number == 9:
            self.roman_number += 'IX'
        elif min_number >= 5:
            self.roman_number += 'V' + (min_number - 5) * 'I'
        elif min_number == 4:
            self.roman_number += 'IV'
        else:
            self.roman_number += min_number * 'I'

    def __str__(self):
        return self.roman_number

    def __add__(self, other):
        roman = copy.copy(self)
        if type(other) is Roman:
            roman.dec_number += other.dec_number
        else:
            roman.dec_number += other
        if roman.dec_number < 0:
            roman.dec_number = 0
        return Roman(roman.dec_number)

    def __sub__(self, other):
        roman = copy.copy(self)
        if type(other) is Roman:
            roman.dec_number -= other.dec_number
        else:
            roman.dec_number -= other
        if roman.dec_number < 0:
            roman.dec_number = 0
        return Roman(roman.dec_number)

    def __mul__(self, other):
        roman = copy.copy(self)
        if type(other) is Roman:
            roman.dec_number *= other.dec_number
        else:
            roman.dec_number *= other
        if roman.dec_number < 0:
            roman.dec_number = 0
        return Roman(roman.dec_number)

    def __mod__(self, other):
        roman = copy.copy(self)
        if type(other) is Roman:
            roman.dec_number //= other.dec_number
        else:
            roman.dec_number //= other
        if roman.dec_number < 0:
            roman.dec_number = 0
        return Roman(roman.dec_number)

    def __le__(self, other):
        roman = self
        if type(other) is Roman:
            return roman.dec_number <= other.dec_number
        else:
            return roman.dec_number <= other

    def __lt__(self, other):
        roman = self
        if type(other) is Roman:
            return roman.dec_number < other.dec_number
        else:
            return roman.dec_number < other

    def __ge__(self, other):
        roman = self
        if type(other) is Roman:
            return roman.dec_number >= other.dec_number
        else:
            return roman.dec_number >= other

    def __gt__(self, other):
        roman = self
        if type(other) is Roman:
            return roman.dec_number > other.dec_number
        else:
            return roman.dec_number > other

    def __eq__(self, other):
        roman = self
        if type(other) is Roman:
            return roman.dec_number == other.dec_number
        else:
            return roman.dec_number == other

    def __ne__(self, other):
        roman = self
        if type(other) is Roman:
            return roman.dec_number != other.dec_number
        else:
            return roman.dec_number != other

class Roman:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        j = self.number
        while j > 0:
            for _ in range(j // val[i]):
                roman_num += syb[i]
                j -= val[i]
            i += 1
        return f'{roman_num}'

    def __add__(self, other:'Roman'):
        roman_new = self.number + other.number
        return Roman(roman_new)

    def __sub__(self, other:'Roman'):
        roman_new = self.number - other.number
        return Roman(roman_new)

    def __mul__(self, mul):
        roman_new = self.number * mul
        return Roman(roman_new)

    def __floordiv__(self, div):
        roman_new = self.number // div
        return Roman(roman_new)

    def __gt__(self, other:'Roman'):
        return self.number > other.number

    def __eq__(self, other:'Roman'):
        return self.number == other.number


# Пример:
n1 = Roman(10)
n2 = Roman(14)
print(n1)  # X
print(n2)  # XIV
n3 = n1 + n2
print(n3)  # XXIV
n3 *= 2
print(n3)  # XLVIII
n1 *= 5
print(n1)
n1 //= 10
print(n1)
if n1 > n2:
    print(f'{n1} больше {n2}')
else:
    print(f'{n1} меньше {n2}')
n3 = Roman(3000)
n4 = Roman(30000)
if n3 != n4:
    print(f'{n3} не равно {n4}')
else:
    print(f'{n3} равно {n4}')

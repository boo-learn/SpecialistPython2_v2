# Задание:
# Напишите класс для работы с римскими цифрами.
# Подробнее про Римские цифры тут: http://graecolatini.bsu.by/htm-different/num-converter-roman.htm
class Roman:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        value = self.number
        for i, number in enumerate(numbers):
            temp_val = value // number
            if temp_val > 0:
                result += letters[i] * temp_val
                value = value % number
        return result

    def __add__(self, other):
        return Roman(self.number + other.number)

    def __sub__(self, other):
        return Roman(self.number - other.number)

    def __mul__(self, other):
        return Roman(self.number * other)

    def __floordiv__(self, other):
        if type(other) is int:
            return Roman(self.number // other)
        else:
            return Roman(self.number // other.number)

    def __gt__(self, other):
        return self.number > other.number

    def __lt__(self, other):
        return self.number < other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number


n1 = Roman(10)
n2 = Roman(14)
print(n1)  # X
print(n2)  # XIV
n3 = n1 + n2
print(n3)  # XXIV
n3 *= 2
print(n3)  # XLVIII

n1986 = Roman(1986)
print('1986', n1986)

n_floordiv = n1986 // n2
print("n_floordiv", n_floordiv)

print("n1>n2", n1 > n2)
print("n1<n2", n1 < n2)
print("n1==n2", n1 == n2)
print("n1!=n2", n1 != n2)

# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        s, denom = fraction_str.split("/")
        if " " in s:
            int_num, num = s.split(" ")
            if int_num[0]=="-":
                num = -int(num) + int(int_num) * int(denom)
            else:
                num = int(num) + int(int_num) * int(denom)
        else:
            num = int(s)
        self.numerator = num  # числителя
        self.denominator = int(denom)  # знаменатель
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе

    def __str__(self):
        minus=""
        if self.numerator<0:
            minus="-"
        if self.numerator % self.denominator == 0:
            return f"{self.numerator // self.denominator}"
        if self.numerator//self.denominator>=1 or (minus=="-" and -self.numerator//self.denominator>=1):

            return f"{minus}{abs(self.numerator)//self.denominator} {abs(self.numerator)%self.denominator}/{self.denominator}"
        return f"{self.numerator}/{self.denominator}"

    def __add__(self,other):
        new_num=self.numerator*other.denominator+self.denominator*other.numerator
        new_denom=self.denominator*other.denominator
        return Fraction(f"{new_num}/{new_denom}")
    def __sub__(self,other):
        new_num = self.numerator * other.denominator - self.denominator * other.numerator
        new_denom = self.denominator * other.denominator
        return Fraction(f"{new_num}/{new_denom}")
    def __mul__(self,other):
        new_num = self.numerator * other.numerator
        new_denom = self.denominator * other.denominator
        return Fraction(f"{new_num}/{new_denom}")
    


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

# TODO: Задание: реализуйте операции с дробями
# Примечание: в начальной реализации получившиеся дроби упрощать не требуется.
# При операциях с дробями их можно приводить к максимальному общему знаменателю.

# Сложение
f_sum = f1 + f2
print(f"{f1} + {f2} = {f_sum}")
# Вычитание
f_sub = f3 - f4
print(f"{f3} - {f4} = {f_sub}")
# Умножение
f_mult = f3 * f4
print(f"{f3} * {f4} = {f_mult}")
# Сравнение (> < == != <= >=)
if f5 > f4:
    print(f"{f5} > {f4}")
elif f5 < f4:
    print(f"{f5} < {f4}")
else:
    print(f"{f5} = {f4}")

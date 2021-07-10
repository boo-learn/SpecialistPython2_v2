# Задание "Простые дроби"

class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        pair = fraction_str.split()
        if len(pair) == 2:
            hole = int(pair[0])
        else:
            hole = 0
        f = pair[-1]
        numerator = int(f.split("/")[0])
        denominator = int(f.split("/")[1])
        self.numerator = numerator + hole * denominator  # числителя
        self.denominator = denominator  # знаменатель
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: -3 5/7
        """
        hole = self.numerator // self.denominator
        num = self.numerator % self.denominator
        return f"{hole} {num}/{self.denominator}"
    
    def __f_hole__(self):
        hole = self.numerator // self.denominator
        return f"{hole}"

    def __add__(self, other_f):
        if self.denominator != other_f.denominator:
            new_denominator = self.denominator * other_f.denominator
            new_numerator = self.numerator + other_f.denominator + other_f.numerator + self.denominator
        else:
            new_denominator = self.denominator
            new_numerator = self.numerator + other_f.numerator
            
        return Fraction(f'{new_numerator}/{new_denominator}')
        
    

# Примеры создания дробей:
f1 = Fraction("4/15")
#print(f1)
f2 = Fraction("11/15")
#print(f2)

f3 = f1 + f2
print(f3)

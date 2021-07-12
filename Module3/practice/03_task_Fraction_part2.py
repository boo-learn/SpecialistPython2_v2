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
        
        a = self.numerator
        b = self.denominator
         
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        
        self.numerator = self.numerator /(a+b)
        self.denominator = self.denominator /(a+b)

    def __str__(self):
         hole = self.numerator // self.denominator
        num = self.numerator % self.denominator
        return f"{hole} {num}/{self.denominator}"
    
dr = Fraction('20/30')
print(dr)

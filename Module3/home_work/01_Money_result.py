class Money:

    def __init__(self, rub, kopeyka):
        self.rub = rub
        self.kopeyka = kopeyka


    def __str__(self):
        all_in_kop = float(self.rub  + self.kopeyka / 100)
        result = str(round(all_in_kop, 2)).split('.')
        return f"{int(result[0])}руб {int(result[1])}коп"
        

    def __add__(self, other):
        all_self_kop = float(self.rub  + self.kopeyka / 100)
        all_other_kop = float(other.rub  + other.kopeyka / 100)
        sum = all_self_kop + all_other_kop
        result = str(round(sum, 2)).split('.')
        if (len(result[1])) == 1:
            return f"{int(result[0])}руб {int(result[1])*10}коп"
        return f"{int(result[0])}руб {int(result[1])}коп"    
        

    def __sub__(self, other):
        all_self_kop = float(self.rub  + self.kopeyka / 100)
        all_other_kop = float(other.rub  + other.kopeyka / 100)
        sub = all_self_kop - all_other_kop
        result = str(round(sub, 2)).split('.')
        if (len(result[1])) == 1:
            return f"{int(result[0])}руб {int(result[1])*10}коп"
        return f"{int(result[0])}руб {int(result[1])}коп"


    def __mul__(self, num):
        all_in_kop = float(self.rub  + self.kopeyka / 100)
        mul = all_in_kop * num
        result = str(round(mul, 2)).split('.')
        if (len(result[1])) == 1:
            return f"{int(result[0])}руб {int(result[1])*10}коп"
        return f"{int(result[0])}руб {int(result[1])}коп"
    

    def __gt__(self, other):
        all_self_kop = float(self.rub  + self.kopeyka / 100)
        all_other_kop = float(other.rub  + other.kopeyka / 100)
        if all_self_kop > all_other_kop:
            return True
        else:
            return False
        

    def __lt__(self, other):
        all_self_kop = float(self.rub  + self.kopeyka / 100)
        all_other_kop = float(other.rub  + other.kopeyka / 100)
        if all_self_kop < all_other_kop:
            return True
        else:
            return False
        

    def __eq__(self, other):
        all_self_kop = float(self.rub  + self.kopeyka / 100)
        all_other_kop = float(other.rub  + other.kopeyka / 100)
        if all_self_kop == all_other_kop:
            return True
        else:
            return False
        

    def __ne__(self, other):
        all_self_kop = float(self.rub  + self.kopeyka / 100)
        all_other_kop = float(other.rub  + other.kopeyka / 100)
        if all_self_kop != all_other_kop:
            return True
        else:
            return False
        

    def __mod__(self, percent):
        all_self_kop = float(self.rub  + self.kopeyka / 100)
        percent__self = all_self_kop * (percent/100)
        result = str(round(percent__self, 2)).split('.')
        if (len(result[1])) == 1:
            return f"{int(result[0])}руб {int(result[1])*10}коп"
        return f"{int(result[0])}руб {int(result[1])}коп"
        


m = Money(20, 6)
s = Money(3, 1)

print(s)
print(m + s)
print(m - s)
print(s * 3)
print(m > s)
print(m < s)
print(m == s)
print(m != s)
print(m % 31)

class Money:
    def __init__(self, rub: int=0,penny: int=0):
        if type(rub)==int:
            self.rub = rub
        if type(penny) == int:
            self.penny = penny % 100
            self.rub += penny // 100
    def __add__(self,other_sum):
        return Money(self.rub + other_sum.rub,self.penny + other_sum.penny)

    def __sub__(self, other_sum):
        return Money(self.rub - other_sum.rub, self.penny - other_sum.penny)
    def __mul__(self, mult_k): #для умножения числа на деньги(хоть не логично) надо перегружать для инта
        return Money(self.rub*mult_k, self.penny*mult_k)
    def __lt__(self,other_sum):
        return self.rub<=other_sum.rub and self.penny<other_sum.penny
    def __gt__(self,other_sum):
        return self.rub>=other_sum.rub and self.penny>other_sum.penny
    def __eq__(self,other_sum):
        return self.rub==other_sum.rub and self.penny==other_sum.penny
    def __str__(self):
        return f'{self.rub} руб. {self.penny} коп.'

money_sum1 = Money(20, 160)
money_sum2 = Money(21, 60)
rez = money_sum1*2
if money_sum1==money_sum2:
    print(rez)

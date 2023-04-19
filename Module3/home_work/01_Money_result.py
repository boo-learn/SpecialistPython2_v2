
class Money:
    def __init__(self, rub, cop):
        if cop >= 100:
            self.rub = rub + cop//100
            self.cop = cop%100
        else:
            self.rub = rub
            self.cop = cop

    def do_better(self, rub, cop):
        if cop >= 100:
            self.rub = rub + cop//100
            self.cop = cop%100
        else:
            self.rub = rub
            self.cop = cop
        return self.rub, self.cop

    def __add__(self, other_sum):
        self.rub += other_sum.rub
        self.cop += other_sum.cop
        if self.cop >= 100:
            self.rub = self.rub + self.cop//100
            self.cop = self.cop%100
        return self

    def __str__(self):
        return f'{self.rub}руб {self.cop}коп'



money_sum1 = Money(20, 440)
print(money_sum1)

money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

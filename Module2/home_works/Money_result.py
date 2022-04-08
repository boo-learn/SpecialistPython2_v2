class Money:
    def __init__(self, roubles:int=0, cop:int=0):
        self.roubles, self.cop = self.count(roubles, cop)

    def count(self, roubles:int=0, cop:int=0):
        """
        Возвращает число рублей и копеек с минимальным значением копеек,
        деньги могут быть отрицательными, но тогда знак и у рубля и у копеек должен быть одинаковым
        """
        znak_cop = 1 if cop >= 0 else -1
        znak_roubles = 1 if roubles >= 0 else -1
        if znak_roubles != znak_cop and roubles != 0:
            znak_cop = znak_roubles
        else:
            znak_roubles = znak_cop
        cop = abs(cop)
        roubles = abs(roubles)
        if cop >= 100:
            dop = cop // 100
            cop -= 100 * dop
            return znak_roubles * (roubles + dop), znak_cop * cop
        else:
            return znak_roubles * roubles, znak_cop *cop

    def __str__(self):
        return f"{self.roubles}р {self.cop}k"

    def __add__(self, other_sum):
        return Money(self.roubles + other_sum.roubles, self.cop + other_sum.cop)

    def __gt__(self, other_sum):
        """
        Money > Money
        """
        if self.roubles == other_sum.roubles and self.cop > other_sum.cop:
            return True
        elif self.roubles > other_sum.roubles:
            return True
        else:
            return False

    def __eq__(self, other_sum):
        """
        Money == Money
        """
        if self.roubles == other_sum.roubles and self.cop == other_sum.cop:
            return True
        else:
            return False

    def __le__(self, other_sum):
        """
        Money <= Money
        """
        if self > other_sum:
            return False
        else:
            return True

    def __lt__(self, other_sum):
        """
        Money < Money
        """
        if self > other_sum or self == other_sum:
            return False
        else:
            return True

    def __ne__(self, other_sum):
        """
        Money != Money
        """
        if self.roubles != other_sum.roubles or self.cop != other_sum.cop:
            return True
        else:
            return False

    def __ge__(self, other_sum):
        """
        Money >= Money
        """
        if other_sum <= self:
            return True
        else:
            return False

    def __sub__(self, other_sum):
        """
        Money - Money
        """
        if other_sum.cop > self.cop:
            return Money(self.roubles - 1 - other_sum.roubles, self.cop + 100 - other_sum.cop)
        else:
            return Money(self.roubles - other_sum.roubles, self.cop - other_sum.cop)

    def __mul__(self, number:int=1):
        """
        Money * int
        """
        cops = 100 * self.roubles + self.cop
        return Money(0, cops * number)

    def __mod__(self, procent:int=100):
        """
        procent from Money
        """
        cops = 100 * self.roubles + self.cop
        return Money(0, round(cops * procent/100))


if __name__ == "__main__":
    sum1 = Money(20, 220)
    sum2 = Money(20, 200)
    print(sum1+sum2)
    print(sum1*2)
    sum3 = Money(-20, -20)
    print(sum1)
    print(sum3)
    print(sum3 + sum1)
    print(f"Половина от {sum3} = {sum3 % 50}")

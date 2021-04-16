class Money:
    def __init__(self, whole=0, fractional=0):
        self.whole = self.__validate_input(whole, 'whole')
        self.fractional = self.__validate_input(fractional, 'fractional')
        self.name = 'Рубль'
        self.name_plural = 'Рубли'

    def __str__(self):
        return f'{self.name_plural} {self.whole}.{self.fractional}'

    def __add__(self, other):
        fractional = self.fractional + other.fractional
        subwhole = 0
        if fractional >= 100:
            subwhole = fractional // 100
            fractional = fractional % 100
        whole = subwhole + self.whole + other.whole
        return Money(whole, fractional)

    def __sub__(self, other):
        fractional = self.fractional - other.fractional
        subwhole = 0
        if fractional < 0:
            fractional = 100 - abs(fractional)
            subwhole = -1
        whole = subwhole + self.whole - other.whole
        return Money(whole, fractional)


    def __validate_input(self, value, _type):
        if _type == 'whole':
            try:
                res = int(value)
            except ValueError:
                raise ValueError(f'{self.name_plural} должны быть целым числом')
        elif _type == 'fractional':
            if value >= 100:
                raise ValueError('Дробная часть не может быть больше чем 99')
            try:
                res = int(value)
            except ValueError:
                raise ValueError(f'Дробная часть должна быть целым числом (так надо)')
        else:
            raise ValueError('Неправильно передан парамент _type, должен быть либо "whole", либо "fractional"')
        return res


if __name__ == '__main__':
    money1 = Money(1, 30)
    money2 = Money(1, 70)
    money3 = money1 + money2
    print(money1)
    print(money3)
    money4 = money3 - Money(1, 1)
    print(money4)

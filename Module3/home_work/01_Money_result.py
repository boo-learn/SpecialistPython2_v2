class Money:
    def __init__(self, rubles: float, cents: float):
        self.rubles = rubles
        self.cents = cents
        self.float_view = self.rubles + self.cents / 100
        # self.actual_view = self.result_rub()
        self.actual_view = [self.rubles + self.cents // 100, self.cents % 100]

    def __getitem__(self, index):
        self.list = [self.rubles, self.cents]
        return self.list[index]

    def result_rub(self, other=(0,0)):
        rub_sum = self.rubles + other[0]
        cent_sum = self.cents + other[1]
        result_all = Money(rub_sum + cent_sum // 100, cent_sum % 100)
        return result_all

    def __str__(self):
        self.actual_view = self.result_rub()
        if self.actual_view[1] == 0:
            return f'{self.actual_view[0]}руб'
        else:
            return f'{self.actual_view[0]}руб {self.actual_view[1]}коп'

    def __add__(self, other):
        rub_sum = self.rubles + other[0]
        cent_sum = self.cents + other[1]
        result_all = Money(rub_sum + cent_sum // 100, cent_sum % 100)
        return result_all

    def __sub__(self, other):
        rub_sum = self.rubles - other[0]
        cent_sum = self.cents - other[1]
        result_all = Money(rub_sum + cent_sum // 100, cent_sum % 100)
        return result_all

    def __mul__(self, other:int):
        rub_sum = self.rubles * other
        cent_sum = self.cents * other
        result_all = Money(rub_sum + cent_sum // 100, cent_sum % 100)
        return result_all

    def __gt__(self, other):
        return self.float_view > other.float_view

    def __lt__(self, other):
        return self.float_view < other.float_view

    def __eq__(self, other):
        return self.float_view == other.float_view



m1 = Money(20, 10)
m2 = Money(20, 10)
print(m1.float_view)
print(m1, m2)
print(m1 > m2, m1 < m2, m1 == m2)
print(m1 + m2)
print(m1 - m2)
print(m1 * 5)
#print(m1 + m2)

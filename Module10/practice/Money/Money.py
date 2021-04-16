class Money():
    def __init__(self, rubs, kop):
        self.rubs = rubs
        self.kop = kop
        self._round()

    def _round(self):
        if self.kop >= 100:
            r, k = divmod(self.kop, 100)
            self.rubs += r
            self.kop = k

    def __repr__(self):
        return (f'{self.rubs}руб {self.kop}коп')

    def __add__(self, other):
        self.rubs += other.rubs
        self.kop += other.kop
        self._round()
        return Money(self.rubs, self.kop)

    def __sub__(self, other):
        if self.kop - other.kop < 0:
            self.rubs -= 1
            self.kop += 100
        self.rubs -= other.kop
        self.kop -= other.kop
        self._round()
        return Money(self.rubs, self.kop)

    def __mul__(self, other):
        if type(other) == int:
            self.rubs * other
            self.kop * other
            self._round()
            return Money(self.rubs, self.kop)
        raise TypeError("В задании было умножение только на целое число :)")

    def __gt__(self, other):
        return (self.kop + self.rubs * 100) > (other.kop + other.rubs * 100)

    def __lt__(self, other):
        return (self.kop + self.rubs * 100) < (other.kop + other.rubs * 100)

    def __eq__(self, other):
        return (self.kop + self.rubs * 100) == (other.kop + other.rubs * 100)

    def __ne__(self, other):
        return (self.kop + self.rubs * 100) != (other.kop + other.rubs * 100)

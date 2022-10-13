class Roman:
    def __init__(self, number):
        self.number = number


    def __str__(self):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[self.number // 1000]
        h = hunds[self.number // 100 % 10]
        te = tens[self.number // 10 % 10]
        o = ones[self.number % 10]

        return t + h + te + o

    def __add__(self, other):
        return Roman(self.number + other.number)

    def __sub__(self, other):
        return Roman(self.number - other.number)

    def __mul__(self, other):
        if type(other) == Roman:
            return Roman(self.number * other.number)
        else:
            return Roman(self.number * other)

    def __gt__(self, other):
        return self.number > other.number

    def __lt__(self, other):
        return self.number < other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number
    def __floordiv__(self, other):
        if type(other) == Roman:
            return Roman(self.number // other.number)
        else:
            return self.number // other

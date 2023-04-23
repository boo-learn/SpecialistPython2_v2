class Roman:
    ROMANS = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

    def __init__(self, dec: int):
        self.__dec = dec
        self.__dec_copy = dec
        self.__rom = []
        self.__convert()

    def __str__(self):
        return ''.join(self.__rom)

    def dec(self):
        return self.__dec

    def rom(self):
        return ''.join(self.__rom)

    def __convert(self):
        m_s = self.__dec_copy // 1000
        self.__dec_copy = self.__dec_copy % 1000
        self.__rom += Roman.ROMANS[1000] * m_s

        d_s = self.__dec_copy // 500
        if d_s:
            c_s = (self.__dec_copy - 500) // 100
            if c_s == 4:
                self.__rom += Roman.ROMANS[100] + Roman.ROMANS[1000]
            else:
                self.__rom += Roman.ROMANS[500] + Roman.ROMANS[100] * c_s
        else:
            c_s = self.__dec_copy // 100
            if c_s:
                self.__rom += Roman.ROMANS[100] * c_s

        self.__dec_copy = self.__dec_copy % 100
        l_s = self.__dec_copy // 50
        if l_s:
            x_s = (self.__dec_copy - 50) // 10
            if x_s == 4:
                self.__rom += Roman.ROMANS[10] + Roman.ROMANS[100]
            else:
                self.__rom += Roman.ROMANS[50] + Roman.ROMANS[10] * x_s
        else:
            x_s = self.__dec_copy // 10
            if x_s:
                self.__rom += Roman.ROMANS[10] * x_s

        self.__dec_copy = self.__dec_copy % 10
        v_s = self.__dec_copy // 5
        if v_s:
            i_s = self.__dec_copy - 5
            if i_s == 4:
                self.__rom += Roman.ROMANS[1] + Roman.ROMANS[10]
            else:
                self.__rom += Roman.ROMANS[5] + Roman.ROMANS[1] * i_s
        else:
            if self.__dec_copy == 4:
                self.__rom += Roman.ROMANS[1] + Roman.ROMANS[5]
            else:
                self.__rom += Roman.ROMANS[1] * self.__dec_copy

    def __add__(self, other):
        return Roman(self.__dec + other.__dec)

    def __sub__(self, other):
        return Roman(self.__dec - other.__dec)

    def __mul__(self, k):
        return Roman(self.__dec * k)

    def __floordiv__(self, other):
        return Roman(self.__dec // other.__dec)

    def __gt__(self, other):
        return self.__dec > other.__dec

    def __lt__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        return self.__dec == other.__dec

    def __ne__(self, other):
        return not self.__eq__(other)

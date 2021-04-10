class Fraction:
    def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
        pair = fraction_str.split()
        if len(pair) == 2:
            whole = int(pair[0])
            f = pair[1].split('/')
            self.numerator = int(f[0])
            self.denominator = int(f[1])
            self.numerator += whole * self.denominator
        else:
            f = pair[0].split('/')
            self.numerator = int(f[0])
            self.denominator = int(f[1])

    def __str__(self):
        whole = self.numerator // self.denominator
        numerator = self.numerator - whole*self.denominator
        return f"{whole or ''} {numerator}/{self.denominator}"

    def __add__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d//self.denominator)
        numerator2 = other_f.numerator * (common_d//other_f.denominator)
        common_n = numerator1 + numerator2
        return Fraction(f"{common_n}/{common_d}")

    def __sub__(self, other_f):
        if self.denominator == other_f.denominator:
            common_d = self.denominator
        else:
            common_d = self.denominator * other_f.denominator
        numerator1 = self.numerator * (common_d//self.denominator)
        numerator2 = other_f.numerator * (common_d//other_f.denominator)
        common_n = numerator1 - numerator2
        return Fraction(f"{common_n}/{common_d}")

	def __mul__(self, other_f):
		new_n = self.numerator * other_f.numerator
		new_d = self.denominator * other_f.denominator
		return Fraction(f"f1 * f2 = {new_n}/{new_d}")

	def add_sc(self, sc):
		other_n = sc * self.denominator
		other_d = self.denominator
		new_n = self.numerator + other_n
		return Fraction(f"{new_n}/{other_d}"


	def __cmp__(self, other_f):
		if self.denominator == other_f.denominator:
			if self.numeratot > other_f.numerator:
				return f'({self.numerator}/{self.denominator} > {other_f.numerator}/{other_f.denominator}'
			elif self.numeratot < other_f.numerator:
				return f'({self.numerator}/{self.denominator} < {other_f.numerator}/{other_f.denominator}'
			else:
				return f'({self.numerator}/{self.denominator} = {other_f.numerator}/{other_f.denominator}'
		else:
				den_1 = self.denominator * other_f.denominator = den_2
				num_1 = self.numerator * othet_f.denominator
				num_2 = other_f.numerator * self.denominator
				if num_1 > num_2:
					return f'({self.numerator}/{self.denominator} > {other_f.numerator}/{other_f.denominator})'
				elif num_1 < num_2:
					return f'({self.numerator}/{self.denominator} < {other_f.numerator}/{other_f.denominator})'
				else:
					return f'({self.numerator}/{self.denominator} = {other_f.numerator}/{other_f.denominator})'

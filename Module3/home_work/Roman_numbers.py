class Roman:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def convertation(num):
        romano = ''
        if num // 1000:
            romano += 'M' * (num // 1000)
        num = num % 1000
        if num // 500:
            if num // 100 == 9:
                romano = romano + 'CM'
            else:
                sum_c = num // 100 - 5
                romano = romano + 'D'
                if sum_c > 0:
                    romano = romano + 'C' * sum_c
        else:
            if num // 100 == 4:
                romano = romano + 'CD'
            else:
                sum_c = num // 100
                if sum_c > 0:
                    romano = romano + 'C' * sum_c

        num = num % 100
        if num // 50:
            if num // 10 == 9:
                romano = romano + 'XC'
            else:
                sum_c = num // 10 - 5
                romano = romano + 'L'
                if sum_c > 0:
                    romano = romano + 'X' * sum_c
        else:
            if num // 10 == 4:
                romano = romano + 'XL'
            else:
                sum_c = num // 10
                if sum_c > 0:
                    romano = romano + 'X' * sum_c

        num = num % 10
        if num // 5:
            if num == 9:
                romano = romano + 'IX'
            else:
                sum_c = num - 5
                romano = romano + 'V'
                if sum_c > 0:
                    romano = romano + 'I' * sum_c
        else:
            if num == 4:
                romano = romano + 'IV'
            else:
                sum_c = num
                if sum_c > 0:
                    romano = romano + 'I' * sum_c

        return romano


    def __repr__(self):
        return Roman.convertation(self.number)

    def __add__(self, other):
        sum_romano = self.number + other.number
        return Roman.convertation(sum_romano)

    def __sub__(self, other):
        sub_romano = self.number - other.number
        return Roman.convertation(sub_romano)

    def __mul__(self, num):
        return Roman.convertation(self.number * num)

    def __rmul__(self, num):
        return Roman.convertation(self.number * num)

    def __floordiv__(self, num):
        return Roman.convertation(self.number // num)

    def __rfloordiv__(self, num):
        return Roman.convertation(self.number // num)



    def __eq__(self, other):
        if self.number == other.number:
            return f'Число {Roman.convertation(self.number)} равно {Roman.convertation(other.number)}'
        else:
            return f'Число {Roman.convertation(self.number)} не равно {Roman.convertation(other.number)}'

    def __ne__(self, other):
        return self.number != other.number

    def __gt__(self, other):
        if int(self.number) > int(other.number):
            return f'Число {Roman.convertation(self.number)} больше чем {Roman.convertation(other.number)}'
        else:
            return f'Число {Roman.convertation(self.number)} не больше чем {Roman.convertation(other.number)}'

    def __lt__(self, other):
        if int(self.number) < int(other.number):
            return f'Число {Roman.convertation(self.number)} меньше чем {Roman.convertation(other.number)}'
        else:
            return f'Число {Roman.convertation(self.number)} не меньше числа {Roman.convertation(other.number)}'






n1 = Roman(10)
n2 = Roman(14)
print(n1)  # X
print(n2)  # XIV
n3 = n1 + n2
print(n3)  # XXIV
n1 *= 2
print(n1)  # XLVIII

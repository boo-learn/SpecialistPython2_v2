
class Roman_num:
    def __init__(self, arabic_num):
        self.roman_num=''
        if arabic_num <= 3999:
            self.__arabic_num=arabic_num
            roman_dictionary = {
                'M': 1000,
                'CM': 900,
                'D': 500,
                'CD': 400,
                'C': 100,
                'XC': 90,
                'L': 50,
                'XL': 40,
                'X': 10,
                'IX': 9,
                'V': 5,
                'IV': 4,
                'I': 1,
            }
            for roman in roman_dictionary:
                self.roman_num += arabic_num // roman_dictionary[roman] * roman
                arabic_num %= roman_dictionary[roman]
        else: print("Чисто вышло за пределы")
    def __add__(self, other):
        return  Roman_num(self.__arabic_num+other.__arabic_num)

    def __sub__(self, other):
        return Roman_num(self.__arabic_num - other.__arabic_num)
    def __mul__(self, other):
        return Roman_num(self.__arabic_num*other.__arabic_num)
    def __truediv__(self, other):
        return Roman_num(self.__arabic_num // other.__arabic_num)

    def __lt__(self, other):
        return self.__arabic_num < other.__arabic_num

    def __gt__(self, other):
        return self.__arabic_num > other.__arabic_num

    def __eq__(self, other):
        return self.__arabic_num == other.__arabic_num
    def __str__(self):
        return self.roman_num



roman_n1=Roman_num(50)
roman_n2=Roman_num(40)
print((roman_n1 / roman_n2))


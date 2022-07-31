Roman_arabic_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 5000: "/"}


class Roman:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.Arabic_to_roman()

    def __add__(self, other):
        return Roman(self.number + other.number)

    def __sub__(self, other):
        return Roman(self.number - other.number)

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.number < other.number

    def __gt__(self, other):
        return self.number > other.number

    def __mul__(self, multiple: int):
        new = Roman(self.number * multiple)
        return new.Arabic_to_roman()

    def Arabic_to_roman(self):

        self.roman_string = ''

        self.thousands_whole = self.number // 1000
        self.thousands_remain = self.number % 1000
        self.five_hundreds_whole = self.thousands_remain // 500
        self.five_hundreds_remain = self.thousands_remain % 500
        self.hundreds_whole = self.five_hundreds_remain // 100
        self.hundreds_remain = self.five_hundreds_remain % 100
        self.half_hundreds_whole = self.hundreds_remain // 50
        self.half_hundreds_remain = self.hundreds_remain % 50
        self.tens = self.half_hundreds_remain // 10
        self.units = self.half_hundreds_remain % 10

        if self.thousands_whole < 4:
            part1 = self.thousands_whole * Roman_arabic_dict[1000]
        elif self.thousands_whole == 4:
            part1 = Roman_arabic_dict[5000] + Roman_arabic_dict[1000] + Roman_arabic_dict[5]
        elif 5 < self.thousands_whole < 9:
            part1 = Roman_arabic_dict[5000] + Roman_arabic_dict[5] + (self.thousands_whole - 5) * \
                    Roman_arabic_dict[1000]
        else:
            part1 = Roman_arabic_dict[1000] + Roman_arabic_dict[10] + Roman_arabic_dict[5000]

        if self.hundreds_whole == 4:
            part2 = Roman_arabic_dict[100] + Roman_arabic_dict[1000]
        else:
            part2 = Roman_arabic_dict[500] + Roman_arabic_dict[100] * self.hundreds_whole

        if self.half_hundreds_whole == 4:
            part3 = Roman_arabic_dict[10] + Roman_arabic_dict[100]
        else:
            part3 = Roman_arabic_dict[50]

        if self.tens == 40:
            part4 = Roman_arabic_dict[10] + Roman_arabic_dict[50]
        else:
            part4 = self.tens * Roman_arabic_dict[10]

        if self.units == 5:
            part5 = Roman_arabic_dict[5]
        elif self.units == 9:
            part5 = Roman_arabic_dict[1] + Roman_arabic_dict[10]
        elif 1 < self.units < 5:
            part5 = self.units * Roman_arabic_dict[1]
        else:
            part5 = Roman_arabic_dict[5] + (self.units - 5) * Roman_arabic_dict[1]

        self.roman_string = part1 + part2 + part3 + part4 + part5

        return f"{self.roman_string}"

        # if self.half_hundreds_whole == 9


n1 = Roman(2789)
n2 = Roman(2025)
n3 = n1 + n2
n4 = n2 - n1
n5 = n1 * 2

print(f"Year in arabic {n1.number} converts in year in Roman {n1}")
print(f"Year in arabic {n2.number} converts in year in Roman {n2}")
print(f"Sum year in arabic {n3.number} converts in year in Roman {n3}")
print(f"Diff year in arabic {n4.number} converts in year in Roman {n4}")
print(f"Mult year 1 in arabic {n1.number} by {2} converts in year in Roman {n5}")

if (n1 > n2):
    print(f"Year {n1.number} > Year {n2.number}")
else:
    print(f"Year {n1.number} < Year {n2.number}")


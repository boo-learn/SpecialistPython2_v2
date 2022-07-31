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

        part1 = ''
        part2 = ''
        part3 = ''
        part4 = ''

        if self.thousands_whole < 4:
            part1 = self.thousands_whole * Roman_arabic_dict[1000]
        elif self.thousands_whole == 4:
            part1 = Roman_arabic_dict[5000] + Roman_arabic_dict[1000] + Roman_arabic_dict[5]
        elif self.thousands_whole == 5:
            part1 = Roman_arabic_dict[5000] + Roman_arabic_dict[5]
        elif 5 < self.thousands_whole < 9:
            part1 = Roman_arabic_dict[5000] + Roman_arabic_dict[5] + (self.thousands_whole - 5) * \
                    Roman_arabic_dict[1000]
        else:
            part1 = Roman_arabic_dict[1000] + Roman_arabic_dict[10] + Roman_arabic_dict[5000]

        # print(f"part 1 {part1}")
        # # print(f"five self hundreds {self.five_hundreds_whole}")
        # #
        # # print(f"self hundreds {self.hundreds_whole}")

        if self.five_hundreds_whole == 1 and self.hundreds_whole != 4:
            part2 = Roman_arabic_dict[500] + self.hundreds_whole * Roman_arabic_dict[100]
        elif self.five_hundreds_whole == 1 and self.hundreds_whole == 4:
            part2 = Roman_arabic_dict[100] + Roman_arabic_dict[1000]
        elif self.five_hundreds_whole == 0 and self.hundreds_whole == 4:
            part2 = Roman_arabic_dict[100] + Roman_arabic_dict[500]
        else:
            part2 = self.hundreds_whole * Roman_arabic_dict[100]

        # print(f"part 2 {part2}")
        # print(f"self tens {self.tens}")

        if self.tens == 4:
            part3 = Roman_arabic_dict[10] + Roman_arabic_dict[50]
        elif self.tens == 5:
            part3 = Roman_arabic_dict[50]
        elif self.tens < 4 and self.half_hundreds_whole < 1:
            part3 = Roman_arabic_dict[10] * self.tens
        else:
            part3 = Roman_arabic_dict[50] + Roman_arabic_dict[10] * self.tens

        # print(f"part 3 {part3}")

        if self.units == 5:
            part4 = Roman_arabic_dict[5]
        elif self.units == 0:
            part4 = ''
        elif self.units == 9:
            part4 = Roman_arabic_dict[1] + Roman_arabic_dict[10]
        elif 1 <= self.units < 5:
            part4 = self.units * Roman_arabic_dict[1]
        else:
            part4 = Roman_arabic_dict[5] + (self.units - 5) * Roman_arabic_dict[1]

        # print(f"part 4 {part4}")

        self.roman_string = part1 + part2 + part3 + part4

        return f"{self.roman_string}"


arabic_year1 = int(input("Enter first year in arabic "))
n1 = Roman(arabic_year1)
arabic_year2 = int(input("Enter second year in arabic "))
n2 = Roman(arabic_year2)
multiple_year = int(input("Enter multiple for year 1 "))
n3 = n1 + n2
n4 = n2 - n1
n5 = n1 * multiple_year

print(f"Year in arabic {n1.number} converts in year in Roman {n1}")
print(f"Year in arabic {n2.number} converts in year in Roman {n2}")
print(f"Sum year in arabic {n3.number} converts in year in Roman {n3}")
print(f"Diff year in arabic {n4.number} converts in year in Roman {n4}")
print(
    f"Mult year 1 in arabic {n1.number} by {multiple_year} = {n1.number * multiple_year} converts in year in Roman {n5}")

if (n1 > n2):
    print(f"Year {n1.number} > Year {n2.number}")
else:
    print(f"Year {n1.number} < Year {n2.number}")

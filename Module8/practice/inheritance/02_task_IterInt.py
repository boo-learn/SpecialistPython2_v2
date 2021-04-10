class MyIter():
    def __init__(self, number):
        self.number = number
        self.index = 0

    def __next__(self):
        try:
            digit = int(str(self.number)[self.index])
        except IndexError:
            raise StopIteration
        self.index += 1
        return digit


class IterInt(int):
    def __iter__(self):
        return MyIter(self)



n = IterInt(12346)

for digit in n:
    print("digit = ", digit)

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6

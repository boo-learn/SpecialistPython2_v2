class IterInt(int):
    def __init__(self, integer):
        self.integer = integer
        self.integer_string = str(self.integer)
        self.last_index = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_index is None:
            self.last_index = 0
        else:
            self.last_index += 1
        if self.last_index >= len(self.integer_string):
            raise StopIteration
        return self.integer_string[self.last_index]


n = IterInt(12346)

# print(n[0])

for digit in n:
    print("digit = ", digit)

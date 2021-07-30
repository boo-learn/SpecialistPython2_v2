# Разработать класс IterInt, который наследует функциональность
# стандартного типа int, но добавляет
# возможность итерировать по цифрам числа


class IterInt(int):

    pointer = 0

    def __iter__(self):
        self.pointer = 0
        return self

    def __next__(self):
        if self.pointer >= len(str(self)):
            raise StopIteration
        res = int(str(self)[self.pointer])
        self.pointer += 1
        return res


n = IterInt(12346)

for digit in n:
    print("digit =", digit)

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6

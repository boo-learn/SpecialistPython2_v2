
# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class IterInt(int):

    def __iter__(self):
        self.last_idx = None
        return self

    def __next__(self):
        self.lst = list(str(self))
        for idx, n in enumerate(self.lst):
            self.lst[idx] = int(n)
        if self.last_idx is None:
            self.last_idx = 0
        else:
            self.last_idx += 1
        if self.last_idx >= len(self.lst):
            raise StopIteration
        return self.lst[self.last_idx]


n = IterInt(12346)

for digit in n:
    print("digit = ", digit)

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6

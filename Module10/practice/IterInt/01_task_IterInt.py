# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class IterInt(int):
    def __init__(self, x):
        super().__init__()
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        try:
            num = int(str(self)[self.count])
            self.count += 1
        except IndexError:
            raise StopIteration
        return num


n = IterInt(12346)

for digit in n:
    print("digit = ", digit)

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6

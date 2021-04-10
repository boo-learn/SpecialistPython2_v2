# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class IterInt(int):
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            digit = int(str(self)[self.index])
        except IndexError:
            raise StopIteration
        self.index += 1
        return digit


n = IterInt(12346)

for digit in n:
    print("digit = ", digit)

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6

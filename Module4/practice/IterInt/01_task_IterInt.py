# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class IterInt(int):
    def __init__(self, *args, **kwargs):
        self.last_index = None
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.last_index is None:
            self.last_index = 0
        else:
            self.last_index += 1
        if self.last_index >= len(str(self)):
            raise StopIteration
        return str(self)[self.last_index]


n = IterInt(12346)

for digit in n:
    print("digit = ", digit)

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6

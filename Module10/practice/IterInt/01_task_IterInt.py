# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class IterInt(int):
    def __init__(self, value):
        try:
            self.value = int(value)
        except ValueError:
            raise ValueError(f'Необходимо ввести целое число, вместо этого было введено {type(value)} {value}')
        self.iteration = 0

    def __str__(self):
        return f'IterInt {self.value}'

    def __iter__(self):
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration >= len(str(self.value)):
            self.iteration = 0
            raise StopIteration
        value = int(str(self.value)[self.iteration])
        self.iteration += 1
        return value


n = IterInt(12346)

for digit in n:
    print("digit = ", digit)

n = IterInt('1s23456f')

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6

# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, numb):
        return Vector(self.x * numb, self.y * numb)


vector1 = Vector(0, 5)
vector2 = Vector(5, 0)

print(f'{vector1}')
print(f'{vector2}')
print(f'{(vector1 + vector2)}')
print(f'{(vector1 - vector2)}')
print(f'{(vector1 * 5)}')

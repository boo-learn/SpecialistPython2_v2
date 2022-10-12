# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector'):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other: 'Vector'):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __str__(self):
        return f'{self.x},{self.y}'

    def __mul__(self, n: int):
        x = self.x * n
        y = self.y * n
        return Vector(x, y)


vector1 = Vector(5, 2)
vector2 = Vector(6, 9)

new_vector = vector1 + vector2
print(new_vector)

new_vector = vector1 - vector2
print(new_vector)

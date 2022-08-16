# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector [{self.x}, {self.y}]'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


vector1 = Vector(8, 16)
vector2 = Vector(-5, 3)
vector3 = Vector(-7, -11)
number = 5
print(vector1)
print(vector2)
print(vector3)
print(f'Сумма векторов {vector1} и {vector2}: {vector1 + vector2}')
print(f'Разность векторов {vector2} и {vector3}: {vector2 - vector3}')
print(f'Произведение {vector2} на число {number}: {vector2 * number}')

# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector [{self.x}, {self.y}]'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)
    
    
v1 = Vector(3, 5)
v2 = Vector(13, 5)
v3 = Vector(-3, 5)
print(v1, v2, v3)
print(v1 + v2)
print(v2 - v3)
print(v2 * 3)

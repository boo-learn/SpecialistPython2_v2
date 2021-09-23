# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def minus(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def mult_scalar(self, scl):
        if scl < 0:
            return Vector(self.y * scl, self.x * scl)
        if scl >= 0:
            return Vector(self.x * scl, self.y * scl)

    def __str__(self):
        return f'({self.x}, {self.y})'

v1 = Vector(5, 10)
v2 = Vector(0, -6)
v3 = v1.plus(v2)
v4 = v1.minus(v2)
v5 = v1.mult_scalar(4)
v6 = v2.mult_scalar(-10)
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)

# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / mag, self.y / mag)

v1 = Vector(3, 4)
v2 = Vector(5, 6)
print(v1 + v2)
print(v2 - v1)
print(v1 * 2)
print(2 * v1)
# print(v1.dot(v2))
# print(v1.cross(v2))
# print(v1.magnitude())
# print(v1.normalize())
a = Vector(2, 4)
k = 3
result = k * a
print(result)

a = Vector(2, 4)
k = -3
result = k * a
print(result)

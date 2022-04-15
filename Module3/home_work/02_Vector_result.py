# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector(self.x * -1, self.y * -1)

    def __mul__(self, number: int = 1):
        return Vector(self.x * number, self.y * number)

    def __rmul__(self, number: int = 1):
        return Vector(self.x * number, self.y * number)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector(1, 1)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    v4 = v1 * 3
    v5 = 3 * v1
    print(v3)
    print(v4)
    print(v5)
    print(v3 - v2)
    print(-v3)

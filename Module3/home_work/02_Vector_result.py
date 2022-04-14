# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, point=(0, 0)):
        self.x, self.y = point

    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x, self.y - other.y))

    def __mul__(self, other):
        return Vector((self.x * other, self.y * other))

    def __str__(self):
        return f'{self.x, self.y}'


if __name__ == "__main__":
    vector1 = Vector((0, 5))
    vector2 = Vector((0, 3))
    print(vector1 * 3)

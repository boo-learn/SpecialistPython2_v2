# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x, self.y - other.y))

    def __mul__(self, k):
        return Vector((self.x * k, self.y * k))

    def __str__(self):
        return "V({}, {})".format(self.x, self.y)


v1 = Vector((1, 2))
v2 = Vector((4, 8))

v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * -2

print('Первый вектор v1 =', v1)
print('Второй вектор v2 =', v2)
print('Сложение векторов v1 + v2 = ', v3)
print('Вычитание векторов v1 - v2 = ', v4)
print('Умножение вектора на число v1 * -2 = ', v5)

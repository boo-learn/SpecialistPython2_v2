# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        summa = Vector(0, 0)
        summa.x = self.x + other.x
        summa.y = self.y + other.y
        return summa

    def __sub__(self, other):
        sub = Vector(0, 0)
        sub.x = self.x - other.x
        sub.y = self.y - other.y
        return sub

    def __mul__(self, number=int or float):
        mul = Vector(0, 0)
        mul.x = self.x * number
        mul.y = self.y * number
        return mul

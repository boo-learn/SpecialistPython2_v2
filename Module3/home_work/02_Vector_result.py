# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_vector):
        return self.x + other_vector.x,  self.y + other_vector.y

    def __sub__(self, other_vector):
        return self.x - other_vector.x,  self.y - other_vector.y

    def __mul__(self, scalar):
        return self.x * scalar, self.y * scalar

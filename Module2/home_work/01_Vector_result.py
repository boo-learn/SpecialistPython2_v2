# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md
from math import sqrt

class Vector:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):  # точка начала или конца вектора
        self.x = x2 - x1  # координата вектора х
        self.y = y2 - y1  # координата вектора у

    def __add__(self, other_vector):
        return f'{{{other_vector.x + self.x};{other_vector.y + self.y}}}'

    def __sub__(self, other_vector):
        return f'{{{other_vector.x - self.x};{other_vector.y - self.y}}}'

    def __mul__(self, scalar):
        return f'{{{ scalar * self.x};{scalar * self.y}}}'

class Vector_dlina:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):  # точка начала или конца вектора
        self.x = x2 - x1  # координата вектора х
        self.y = y2 - y1  # координата вектора у

    def dlina(self):
        return sqrt( (self.x ** 2) + (self.y ** 2))

    def __lt__(self, other):
        if self.dlina() == other.dlina():
            return self.dlina() < other.dlina()
        else:
            return self.dlina() < other.dlina()

    def __gt__(self, other):
        if self.dlina() == other.dlina():
            return self.dlina() > other.dlina()
        else:
            return self.dlina() > other.dlina()

    def __str__(self):
        return "Vector(x:{} y:{})".format(self.x, self.y)



vector_1 = Vector(11, 6, 3, 8)
vector_2 = Vector(8, 1, 5, 14)
vector_1_dl = Vector_dlina(11, 6, 3, 8)
vector_2_dl = Vector_dlina(8, 1, 5, 14)

if vector_1_dl < vector_2_dl:
    print(f"{vector_1_dl} меньше {vector_2_dl}")
print("Сумма векторов равна =", vector_1 + vector_2)
print("Разность векторов равна =", vector_2 - vector_1)
print("Умножение вектора на скаляр равна =", vector_1 * 5)

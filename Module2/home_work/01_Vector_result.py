# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # to_str
        return f"[{self.x}, {self.y}]"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return Vector(self.x * factor, self.y * factor)


vector_a = Vector(2, 4)
vector_b = Vector(1, 2)
print(vector_a)
if vector_a == vector_b:
    print(f"Векторы {vector_a} и {vector_b} равны")
else:
    print(f"Векторы {vector_a} и {vector_b} не равны")
print(f"Сумма векторов a и b равна {vector_a + vector_b}")
print(f"Разность векторов a и b равна {vector_a - vector_b}")
print(f"Произведение вектора a и числа 5 равно {vector_a * 5}")

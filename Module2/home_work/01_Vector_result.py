# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Длина вектора
    def len(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)

    # Сложение векторов
    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    # Вычитание векторов
    def __sub__(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    # Умножение на скалярную величину
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Представление вектора в выводе
    def __str__(self):
        return f'Vector({round(self.x, 2)}, {round(self.y, 2)})'


vector1 = Vector(3, 4)
vector2 = Vector(9, 12)

sum = vector1 + vector2

print(f'vector1 = {vector1}, vector1.len() = {vector1.len()}')
print(f'vector2 = {vector2}, vector2.len() = {vector2.len()}')
print(f'sum = {sum}, sum.len() = {sum.len()}')

vector3 = sum - vector2
multp = vector3 * (-3)

print(f'vector3 = {vector3}, vector3.len() = {vector3.len()}')
print(f'multp = {multp}, multp.len() = {multp.len()}')

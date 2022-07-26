class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'vector ({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


a = Vector(2, 1)
b = Vector(-2, 2)
k = -10
print(a)  # Вывод вектора
sum_vectors = a + b
print(sum_vectors)  # Вывод суммы векторов
sub_vectors = a - b
print(sub_vectors)  # Вывод разности векторов
mul_vectors = a * k
print(mul_vectors)  # Вывод умножения вектора на скаляр

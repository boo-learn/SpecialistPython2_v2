class Vector:

    def __init__(self, begin, end):

        self.begin = begin
        self.end = end

    def __str__(self):

        return f'Vector({self.begin}, {self.end})'

    def __add__(self, other_vector):

        return Vector(self.begin + other_vector.begin, self.end + other_vector.end)

    def __sub__(self, other_vector):

        return Vector(self.begin - other_vector.begin, self.end - other_vector.end)

    def __mul__(self, x: int):

        return Vector(self.begin * x, self.end * x)


# ТЕСТИРОВАНИЕ

# Создаем два вектора
vector1 = Vector(2,3)
vector2 = Vector(1,4)

# Тестируем строковое представление
print("Тестируем строковое представление")
print(vector1)
print(vector2)

# Тестируем сумму векторов
print('Тестируем сумму векторов')
vector_sum = vector1 + vector2
print(vector_sum)

# Тестируем разность векторов без дополнительной переменной
print("Тестируем разность векторов без дополнительной переменной")
print(vector1 - vector2)

# Тестируем умножение вектора на число
vector_multiplication = vector1 * 2
print("Тестируем умножение вектора на число")
print(vector_multiplication)

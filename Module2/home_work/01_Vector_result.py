class Vector:
    """Вектор в двухмерном пространстве"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector ({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self

    def __mul__(self, k: int):
        self.x = self.x * k
        self.y = self.y * k
        return self


if __name__ == '__main__':
    print('Задаём два вектора')
    vector1 = Vector(1, 2)
    vector2 = Vector(4, 5)
    print(vector1)
    print(vector2)

    print('Умножим векторы на скаляры')
    vector1 = vector1 * 2
    vector2 = vector2 * -1
    print(vector1)
    print(vector2)

    print('Сложим оба вектора')
    vector3 = vector1 + vector2
    print(vector3)

    print('Вычтем из вектора вектор')
    vector3 = vector1 - vector2
    print(vector3)

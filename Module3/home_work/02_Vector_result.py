class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


vector1 = Vector(2, 5)
vector2 = Vector(1, 15)

vector_result = vector1 + vector2
print(vector_result)

vector_result = vector1 - vector2
print(vector_result)

vector_result = vector1 * -2
print(vector_result)


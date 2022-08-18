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

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

vector1 = Vector(10, 3)
vector2 = Vector(-5, 6)
vector3 = vector1 + vector2
print(vector1, ' + ', vector2, ' = ', vector3)

vector3 = vector1 - vector2
print(vector1, ' - ', vector2, ' = ', vector3)

k = 2

vector3 = vector1 * k
print(vector1, ' * ', k, ' = ', vector3)

vector3 = k * vector1
print(k, ' * ', vector1, ' = ', vector3)

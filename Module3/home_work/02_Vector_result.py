class Vector:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'{self.x}i + {self.y}j'

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        raise ValueError("Число!!")

a = Vector(3, 6)
b = Vector(1, 2)
c = a + b
d = a - b
f = a * 5
print(f"{a}, {b}")
print(c)
print(d)
print(f)

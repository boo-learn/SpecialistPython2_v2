class Vector:
    def __init__(self, x_point, y_point):
        self.x = x_point
        self.y = y_point

    def __str__(self):
        return "Вектор {"+f"{self.x};{self.y}"+"}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


# vek1, vec2 = (Vector(0,5), Vector(0,6))
# print(vek1-vec2)
# print(vek1-vec2)
# print(vek1*3)

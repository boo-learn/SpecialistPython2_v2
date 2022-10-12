class Vector:
    pass

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return "V(x:{} y:{})".format(self.x, self.y)

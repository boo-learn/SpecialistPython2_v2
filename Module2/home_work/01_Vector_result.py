class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, other_vector):
        return (self.x + other_vector.x, self.y + other_vector.y)

    def minus(self, other_vector):
        return (self.x - other_vector.x, self.y - other_vector.y)

    def mult_scalar(self, scl):
        return (self.x * scl, self.y * scl)


v1 = Vector(5, 10)
v2 = Vector(0, -6)
print(v1.plus(v2))
print(v1.minus(v2))
print(v1.mult_scalar(-4))

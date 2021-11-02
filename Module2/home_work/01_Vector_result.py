class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return (self.x, self.y)

    def __add__(self, other_vect):
        return (self.x + other_vect.x, self.y + other_vect.y)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __mul__(self, num):
        return (self.x * num, self.y * num)


vect1 = Vector(3, -5)
vect2 = Vector(2, 3)

print(vect1 + vect2)
print(vect1 - vect2)
print(vect1 * 3)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __add__(self, other_vector):
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector(x, y)

    def __mul__(self, cnt):
        return Vector(self.x * cnt, self.y * cnt)

    def __sub__(self, other_vector):
        return self + (other_vector * -1)


vector1 = Vector(5, 1)
vector2 = Vector(2, 6)
print(vector1, vector2)
vector_sum = vector1 + vector2
print(vector_sum)
vector_sub = vector1 - vector2
print(vector_sub)
vector_mult = vector2 * -1
print(vector_mult)


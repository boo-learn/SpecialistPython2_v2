class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add_vector(self, other_vector):
        new_vector = Vector(self.x + other_vector.x, self.y + other_vector.y)
        return new_vector
    def minus_vector(self,other_vector):
        new_vector = Vector(self.x - other_vector.x, self.y - other_vector.y)
        return new_vector
    def multiplication_vector(self,a):
        new_vector = Vector(self.x * a, self.y * a)
        return new_vector
    def __str__(self):
        return f'Вектор({self.x},{self.y})'

vector1 = Vector(1, 2)
vector2 = Vector(5, 3)

print(vector1.add_vector(vector2))
print(vector2.minus_vector(vector1))
print(vector1.multiplication_vector(3))

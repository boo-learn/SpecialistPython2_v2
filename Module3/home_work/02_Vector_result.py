
class Vector:
    def __init__(self, x, y):
       
        self.x = x
        self.y = y

    def __add__(self, other_vector):

        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):

        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, num):

        return Vector(self.x * num, self.y * num)

    def __str__(self):

        return f"{self.x} {self.y}"
   

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)
v4 = v1 - v2
print(v4)
v5 = v3 * 3
print(v5)

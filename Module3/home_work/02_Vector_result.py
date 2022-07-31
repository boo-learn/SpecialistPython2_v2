class Vector:
    def __init__(self, point_x, point_y):
        self.point_x = point_x  # x point]
        self.point_y = point_y  # y point

    def __str__(self):
        return f'({self.point_x},{self.point_y})'

    def __add__(self, other_vector):
        return Vector(self.point_x + other_vector.point_x, self.point_y + other_vector.point_y)

    def __sub__(self, other_vector):
        return Vector(self.point_x - other_vector.point_x, self.point_y - other_vector.point_y)

    def __mul__(self, skalyar: int):
        return Vector(self.point_x * skalyar,  self.point_y * skalyar)

vector_1 = Vector(2, 0)
vector_2 = Vector(4, 3)
skalyar1 = 4
skalyar2 = -3
vector_sum = vector_1 + vector_2
vector_minus = vector_1 - vector_2
multiple1 = vector_1 * skalyar1
multiple2 = vector_1 * skalyar2

print (f"Vector 1 {vector_1}")
print (f"Vector 2 {vector_2}")
print(f"Vector sum {vector_sum}")
print(f"Vector substraction {vector_minus}")
print (f"{vector_1} multiply by {skalyar1} = {multiple1}")
print (f"{vector_1} multiply by {skalyar2} = {multiple2}")

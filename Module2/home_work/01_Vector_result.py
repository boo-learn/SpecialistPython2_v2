class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_vector):
        return f'a + b = ({self.x + other_vector.x}, {self.y + other_vector.y})'

    def __sub__(self, other_vector):
        return f'a - b = ({self.x - other_vector.x}, {self.y - other_vector.y})'

    def __mul__(self, k):
        return f'a * k = ({self.x * k}, {self.y * k})'


a = Vector(3, 2)
b = Vector(2, 4)


print(a + b)
print(a - b)
print(a * 2)
print(a * -2)

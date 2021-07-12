class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other_v):
        sum_x = self.x + other_v.x
        sum_y = self.y + other_v.y
        return Vector(sum_x, sum_y)

    def __sub__(self, other_v):
        sub_x = self.x - other_v.x
        sub_y = self.y - other_v.y
        return Vector(sub_x, sub_y)

    def __mul__(self, number):
        new_x = self.x * number
        new_y = self.y * number
        return Vector(new_x, new_y)

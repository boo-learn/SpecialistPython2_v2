class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:G}, {self.y:G})"

    def distance_to(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, coef):
        if type(coef) is not int and type(coef) is not float:
            raise ValueError(f"Invalid operation: multiplying Point by {type(coef)}")
        return Point(coef * self.x, coef * self.y)

    def __rmul__(self, coef):
        return self.__mul__(coef)


class Vector:
    def __init__(self, begin, end):
        self.beg = begin
        self.end = end

    def __str__(self):
        return f"({self.beg}, {self.end})"

    def __add__(self, other):
        return Vector(self.beg, self.end + other.end - other.beg)

    def __neg__(self):
        return Vector(self.end, self.beg)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, coef):
        if type(coef) is not int and type(coef) is not float:
            raise ValueError(f"Invalid operation: multiplying Vector by {type(coef)}")
        return Vector(self.beg, self.beg + coef * (self.end - self.beg))

    def __rmul__(self, coef):
        return self.__mul__(coef)


# сложение
v1 = Vector(Point(2, 2), Point(7, 6))
v2 = Vector(Point(5, 6), Point(10, 7))
print(f"{v1} + {v2} = {v1 + v2}")
v1 = Vector(Point(4, 3), Point(5, 8))
v2 = Vector(Point(0, 0), Point(7, 3))
print(f"{v1} + {v2} = {v1 + v2}")
print()
# вычитание
v1 = Vector(Point(0, 0), Point(10, 3))
v2 = Vector(Point(0, 0), Point(2, 4))
print(f"{v1} - {v2} = {v1 - v2}")
v1 = Vector(Point(1, 0), Point(11, 3))
v2 = Vector(Point(1, 2), Point(3, 6))
print(f"{v1} - {v2} = {v1 - v2}")
print()
# умножение на скаляр
v1 = Vector(Point(0, 0), Point(3.5, -6))
n = 2.5
print(f"{v1} * {n} = {n * v1}")
v1 = Vector(Point(2, 2), Point(7, 6))
n = 3
print(f"{v1} * {n} = {n * v1}")
v1 = Vector(Point(2, 3), Point(8, 1))
n = -0.5
print(f"{v1} * {n} = {v1 * n}")


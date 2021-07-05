import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

class Triangle:
    point1 = 0
    point2 = 0
    point3 = 0
    a = 0
    b = 0
    c = 0

    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        self.a = self.point1.dist_to(self.point2)
        self.b = self.point1.dist_to(self.point3)
        self.c = self.point2.dist_to(self.point3)

    def perimeter(self):
        return(self.a + self.b + self.c)

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

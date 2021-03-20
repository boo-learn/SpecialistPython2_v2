import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimetr(self):
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        return a + b + c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        p = self.perimetr()
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        half_perimetr = p / 2
        return math.sqrt(half_perimetr
                         * (half_perimetr - a)
                         * (half_perimetr - b)
                         * (half_perimetr - c))


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(6, 8), Point(-2, 10))
# Задание: найдите площадь и периметр треугольника, реализовав методы

print("Периметр треугольника = ", triangle1.perimetr())
print("Площадь треугольника = ", triangle1.area())

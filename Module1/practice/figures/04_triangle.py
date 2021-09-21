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

    def perimeter(self):
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        return a + b + c

    def area(self):
        pol_perimeter = self.perimeter() / 2
        s = (pol_perimeter - self.point1.dist_to(self.point2)) * (
                    pol_perimeter - self.point2.dist_to(self.point3)) * (
                        pol_perimeter - self.point3.dist_to(self.point1)) ** 0.5
        return s


triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

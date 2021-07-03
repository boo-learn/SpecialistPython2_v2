class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return round(((self.x - other_point.x) ** 2 +
                      (self.y - other_point.y) ** 2) ** 0.5, 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        """
        :return: Периметр треугольника
        """
        return self.point1.dist_to(self.point2) +\
               self.point1.dist_to(self.point3) +\
               self.point2.dist_to(self.point3)

    def area(self):
        """
        :return: Площадь треугольника
        """
        x1, y1, x2, y2, x3, y3 = [self.point1.x, self.point1.y,
                                  self.point2.x, self.point2.y,
                                  self.point3.x, self.point3.y]
        return abs(
            0.5 * ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)))


triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

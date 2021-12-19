class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        dist = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        return dist


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        per = self.point1.dist_to(self.point2) + self.point2.dist_to(self.point3) + self.point3.dist_to(self.point1)
        return per

    def area(self):
        per = self.point1.dist_to(self.point2) + self.point2.dist_to(self.point3) + self.point3.dist_to(self.point1)
        p = per/2
        area_t = (p * (p - self.point1.dist_to(self.point2)) * (p - self.point2.dist_to(self.point3)) * (p - self.point3.dist_to(self.point1))) ** 0.5
        return area_t


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

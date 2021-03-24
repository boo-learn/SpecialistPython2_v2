class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point_1 = p1
        self.point_2 = p2
        self.point_3 = p3

    def perimeter(self):
        a = self.point_1.dist_to(self.point_2)
        b = self.point_1.dist_to(self.point_3)
        c = self.point_2.dist_to(self.point_3)
        return a + b + c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a = self.point_1.dist_to(self.point_2)
        b = self.point_1.dist_to(self.point_3)
        c = self.point_2.dist_to(self.point_3)
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(6, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

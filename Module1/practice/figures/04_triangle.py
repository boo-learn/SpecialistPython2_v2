class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        self.a = self.point1.dist_to(self.point2)
        self.b = self.point2.dist_to(self.point3)
        self.c = self.point3.dist_to(self.point1)

    def perimeter(self):
        # Периметр треугольника
        return self.a + self.b + self.c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        return (self.perimeter() / 2 * (self.perimeter() / 2 - self.a) * \
                                       (self.perimeter() / 2 - self.b) * \
                                       (self.perimeter() / 2 - self.c)) ** 0.5


# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(6, 4))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

print(f"Периметр треугольника = {triangle.perimeter():.1f}")
print(f"Площадь треугольника = {triangle.area():.1f}")

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
        # Находим длины сторон треугольника:
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point1.dist_to(self.point3)
        return a + b + c

    def area(self):
        # Находим длины сторон треугольника:
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point1.dist_to(self.point3)
        # Полу-периметр:
        half_p = (a + b + c) / 2
        # Для нахождения площади, используйте формулу Герона
        return (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))

# Находим площадь и периметр треугольника:
print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

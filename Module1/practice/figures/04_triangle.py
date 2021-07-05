class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ( (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 ) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        return self.p1.dist_to(self.p2) + self.p2.dist_to(self.p3) + self.p3.dist_to(self.p1)

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        return (self.perimeter() / 2
                * (self.perimeter() / 2 - self.p1.dist_to(self.p2))
                * (self.perimeter() / 2 - self.p2.dist_to(self.p3))
                * (self.perimeter() / 2 - self.p3.dist_to(self.p1))
               ) ** 0.5


test_triangle = Triangle(Point(0, 0), Point(0, 3), Point(4, 0))


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы


print(test_triangle.perimeter())
print(test_triangle.area())
print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())

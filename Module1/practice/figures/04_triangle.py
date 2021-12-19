class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, op):
        return ((self.x - op.x) ** 2 + (self.y - op.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        perim = (
            self.point1.dist_to(self.point2)
            + self.point2.dist_to(self.point3)
            + self.point3.dist_to(self.point1)
        )
        return perim

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        p_half = self.perimeter() / 2
        s = (
            p_half
            * (p_half - self.point1.dist_to(self.point2))
            * (p_half - self.point2.dist_to(self.point3))
            * (p_half - self.point3.dist_to(self.point1))
        ) ** 0.5
        return s


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...

area = triangle1.area()
perimeter = triangle1.perimeter()

print("Периметр треугольника = ", perimeter)
print("Площадь треугольника = ", area)

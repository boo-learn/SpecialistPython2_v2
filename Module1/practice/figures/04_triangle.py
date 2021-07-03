class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        ...


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        ...

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        ...


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...

print("Периметр треугольника = ", ...)
print("Площадь треугольника = ", ...)

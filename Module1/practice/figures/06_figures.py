import math
# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, name, p1, p2, p3):
        self.name = name
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
        s = (pol_perimeter * (pol_perimeter - self.point1.dist_to(self.point2)) * (
                    pol_perimeter - self.point2.dist_to(self.point3)) * (
                        pol_perimeter - self.point3.dist_to(self.point1))) ** 0.5
        return s


class Circle:
    def __init__(self, name, center_coords, radius):
        self.name = name
        self.center = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        distance_center_circle = ((self.center[0] - other_circle.center[0])
                                  ** 2 + (self.center[1] - other_circle.center[1]) ** 2) ** 0.5
        sum_radius = self.radius + other_circle.radius
        if distance_center_circle <= sum_radius:
            return True
        else:
            return False

    def area(self):
        return math.pi * self.radius ** 2

figures = [
    Triangle("t1", Point(2, 3), Point(12, 11), Point(10, -2)),
    Triangle("t2", Point(5, 0), Point(-7, 11), Point(10, -12)),
    Triangle("t3", Point(-2, -1), Point(21, 11), Point(23, -22)),
    Circle("c1", (1, 1), 11),
    Circle("c1", (21, 5), 22),
    Circle("c1", (3, 11), 31)
]
print(max([figure.area() for figure in figures]))

# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def __str__(self):
        return f"Triangle: {self.point1}, {self.point2}, {self.point3}"

    def perimeter(self):
        a = self.point1.dist_to(self.point2)
        b = self.point1.dist_to(self.point3)
        c = self.point2.dist_to(self.point3)

        return a + b + c

    def area(self):
        a = self.point1.dist_to(self.point2)
        b = self.point1.dist_to(self.point3)
        c = self.point2.dist_to(self.point3)

        hp = (a + b + c) / 2

        return (hp * (hp - a) * (hp - b) * (hp - c)) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        self.x = center_coords[0]
        self.y = center_coords[1]
        self.radius = radius

    def __str__(self):
        return f"Circle: ({self.x}, {self.y}), {self.radius}"

    def intersect(self, other_circle):
        l = ((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2) ** 0.5
        return l <= self.radius + other_circle.radius

    def area(self):
        return math.pi * self.radius * self.radius


figures = [Triangle(Point(0, 0), Point(0, 10), Point(100, 0)),
           Circle((6, -8), 5),
           Circle((2, 4), 4)]

max_area = 0
for figure in figures:
    if figure.area() > max_area:
        max_area = figure.area()
        max_fig = figure

print(max_fig)

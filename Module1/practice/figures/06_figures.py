# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью

import math

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
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        return a + b + c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        p = self.perimeter() / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = Point(*center_coords)
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        dist = self.center_coords.dist_to(other_circle.center_coords)
        return self.radius + other_circle.radius <= dist
    def area(self):
        return math.pi*(self.radius**2)


figures = [
    Circle((6, -8), 5),
    Circle((2, 4), 4),
    Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
]

first_figure_area = figures[0].area()

for figure in figures:
    if first_figure_area < figure.area():
        first_figure_area = figure.area()

print(first_figure_area)

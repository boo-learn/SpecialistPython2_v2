# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return round(((self.x - other_point.x) ** 2 +
                      (self.y - other_point.y) ** 2) ** 0.5, 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def __str__(self):
        return (f'Triangle: ({self.point1.x}, {self.point1.y}), '
                f'({self.point2.x}, {self.point2.y}),'
                f'({self.point3.x}, {self.point3.y})')

    def perimeter(self):
        """
        :return: Периметр треугольника
        """
        return (self.point1.dist_to(self.point2) +
               self.point1.dist_to(self.point3) +
               self.point2.dist_to(self.point3))

    def area(self):
        """
        :return: Площадь треугольника
        """
        x1, y1, x2, y2, x3, y3 = [self.point1.x, self.point1.y,
                                  self.point2.x, self.point2.y,
                                  self.point3.x, self.point3.y]
        return abs(
            0.5 * ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)))


class Circle:
    def __init__(self, center_coords, radius):
        self.center = center_coords
        self.radius = radius

    def __str__(self):
        return f'Circle: center = ({self.center.x}, {self.center.y}), '\
               f'r = {self.radius}'

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        d = ((self.center.x - other_circle.center.x) ** 2 +
             (self.center.y - other_circle.center.y) ** 2) ** 0.5
        return d < (self.radius + other_circle.radius)

    def area(self):
        """
        :return: Площадь фигуры
        """
        return math.pi * self.radius ** 2


figures = [Triangle(Point(0, 0), Point(1, 0), Point(0, 1)),
           Circle(Point(3, 4), 6)]

print(sorted(figures, key=lambda x: x.area())[-1])

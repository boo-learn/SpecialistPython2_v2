# Используя классы треугольника и окружности из предыдущих задач
# создайте список с произвольным набором фигур
# Найдите и выведите фигуры с наибольшей площадью

# Используя классы треугольника и окружности из предыдущих задач
# создайте список с произвольным набором фигур
# Найдите и выведите фигуры с наибольшей площадью

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

import math


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords=center_coords
        self.radius=radius

    def length(self):
        """
        :return: длину окружности
        """
        # TODO-1: реализуйте метод
        return 2*math.pi*self.radius

    def area(self):
        """
        :return: площадь окружности
        """
        # TODO-2: реализуйте метод
        return math.pi*self.radius

figures = [Circle((6, -8), 5), Circle((2, 4), 4), Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))]

def max_area(figures):
    max_area=0
    for figure in figures:
        cur_area = figure.area()
        if cur_area > max_area:
            max_area=cur_area
            max_figure=figure
    return max_figure

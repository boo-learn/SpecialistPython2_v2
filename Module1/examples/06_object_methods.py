import math
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, other_point):
        return math.sqrt((other_point.x-self.x)**2 + (other_point.y-self.y)**2)


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)


# TODO-2: выведите расстояние между точками используя метод dist_to()
dist = point1.dist_to(point2)
print(f"Расстояние между точками = {dist}")

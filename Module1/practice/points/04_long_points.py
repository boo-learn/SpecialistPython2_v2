import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты

point0 = Point(0, 0)

max_dist = 0
for p in points:
    dist = p.dist_to(point0)
    if dist > max_dist:
        max_dist = dist
        max_p = p


print(f"Координаты наиболее удаленной точки = x: {max_p.x}, y: {max_p.y}, расстояние = {max_dist}")

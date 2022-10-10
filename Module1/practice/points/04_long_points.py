from __future__ import annotations
import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return math.hypot(self.x - other_point.x, self.y - other_point.y)


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
point_zero = Point(0,0)
point_m = 0

for point in points:
    print(f"(x:{point.x}, y:{point.y})")
    dist = point.dist_to(point_zero)
    print("Расстояние между точками = ", dist)
    point_m = max(point_m,dist)

# TODO-1: найдите точку наиболее удаленную от начала координат и выведите ее координаты

print("Координаты наиболее удаленной точки = ", point_m)

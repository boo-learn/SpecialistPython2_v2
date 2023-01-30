from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(20, 0), Point(5, -2), Point(10, -16), Point(-12, 0)]
max1 = 0
for i in points:
    dist = i.dist_to(Point(0, 0))
    if dist > max1:
        max1 = dist

print("Координаты наиболее удаленной точки = ", max1)

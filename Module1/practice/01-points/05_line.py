from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

previous_point = points[0]
lenght = 0
for point in points[1:]:
    lenght += previous_point.dist_to(point)
    previous_point = point


# TODO: Найдите длину ломаной линии

print("Длина ломаной линии = ", lenght)

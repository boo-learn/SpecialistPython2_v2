from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return (((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2)) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

origin_point = Point(0, 0)

# TODO-1: найдите точку наиболее удаленную от начала координат и выведите ее координаты
result = 0.0
for point in points:
    distance = point.dist_to(origin_point)
    if distance > result:
        result = distance

print("Координаты наиболее удаленной точки = ", result)

from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(0, 0), Point(0, 5), Point(0, 7), Point(0, 10), Point(0, 12)]

points_count = len(points)
line_len = 0
for i in range(2, len(points)):
    dist = points[i-1].dist_to(points[i])
    line_len = line_len + dist

print("Длина ломаной линии = ", line_len)

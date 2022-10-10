from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return  ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5



# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

null_xy = Point(0,0)
max = (points[0]).dist_to(null_xy)
sum = 0
for point in points:
    dist = point.dist_to(null_xy)
    print(dist)
    sum += dist
    if dist >= max:
        max = dist
print(max)
print(sum)

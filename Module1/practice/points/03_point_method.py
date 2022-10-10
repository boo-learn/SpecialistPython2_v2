from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x)**2+(self.y - other_point.y)**2)**0.5


# Дано две точки на координатной плоскости
point1 = Point(12, -5)
point2 = Point(2, 7)

dist = point1.dist_to(point2)

print(f"Расстояние между точками = {dist}")

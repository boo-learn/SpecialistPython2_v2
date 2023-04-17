from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
       return((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

point1.dist_to(point2)

# TODO-2: выведите расстояние между точками используя метод dist_to()
print(f"Расстояние между точками = {point1.dist_to(point2)}")

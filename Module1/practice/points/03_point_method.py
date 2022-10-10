from __future__ import annotations

class Point:
    # Конструктор - вызывается автоматически, при создании объекта из класса
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

def distance(p1: Point, p2: Point) -> float:
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

# Создадим несколько объектов
point1 = Point(12, -5)
point2 = Point(2, 7)

print(point1.dist_to(point2))

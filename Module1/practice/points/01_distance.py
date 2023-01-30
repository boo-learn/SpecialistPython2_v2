#Гаврилов Павел Решение

import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """
    Расстояние между двумя точками
    """
    result = math.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y)**2))

    return result


# Даны две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

dist = distance(point1, point2)  # Передаем объекты point1 и point2 в функцию

print("Расстояние между точками = ", dist)


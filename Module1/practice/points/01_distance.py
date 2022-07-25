import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return math.sqrt(
        math.pow((p2.x - p1.x), 2) +
        math.pow((p2.y - p1.y), 2)
    )


# Даны две точки на координатной плоскости
point1 = Point(2, 5)
point2 = Point(5, -2)

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)

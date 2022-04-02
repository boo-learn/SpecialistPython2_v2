from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    d = sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 )
    return d
    """
    Расстояние между двумя точками
    """

# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

dist = distance(point1, point2)  # Передаем объекты point1 и point2 в функцию

print("Расстояние между точками = ", dist)

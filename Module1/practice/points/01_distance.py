class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    d = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    return d


# Дано две точки на координатной плоскости
point1 = Point(10, 4)
point2 = Point(24, 4)

dist = distance(point1, point2)  # Передаем объекты point1 и point2 в функцию

print("Расстояние между точками = ", dist)

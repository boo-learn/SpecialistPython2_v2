class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """
    Расстояние между двумя точками
    """
    a = ((point2.x - point1.x) ** 2) + ((point2.y - point1.y) ** 2) ** 0.5
    return a


# Даны две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(2, 10)

dist = distance(point1, point2)  # Передаем объекты point1 и point2 в функцию

print("Расстояние между точками = ", dist)

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    p1x = p1.x
    p1y = p1.y
    p2x = p2.x
    p2y = p2.y
    result = (((p1x - p2x)**2) + ((p1y - p2y)**2))**0.5
    return float(result)

# Даны две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

dist = distance(point1, point2)  # Передаем объекты point1 и point2 в функцию

print("Расстояние между точками = ", dist)

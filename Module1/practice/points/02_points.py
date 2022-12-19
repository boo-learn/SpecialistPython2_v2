class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)


def distance(p1: Point, p2: Point) -> float:
    """
    Расстояние между двумя точками
    """
    dist = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    return dist


for p in points:
    print(distance(random_point, p))

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


# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

i = 1
for pt in points:
    dist = distance(random_point, pt)
    print(f"Расстояние от точки {i}: {dist}")
    i += 1

мое решение!
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** .5
dist1 = distance(points[0], points[1])
dist2 = distance(points[1], points[2])
dist3 = distance(points[3], points[4])
dist4 = distance(points[0], points[4])
dist = dist1 + dist2 + dist3 + dist4
print("Длина ломаной линии = ", dist)

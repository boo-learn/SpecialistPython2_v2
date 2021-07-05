class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(pt1: Point, pt2: Point):
    """
    Расстояние между двумя точками
    """
    return ((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2)**0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


len_max = 0
dist = 0
zero_point = Point(0, 0)
max_point = points[0]
for a in points:
    dist = distance(a, zero_point)
    if dist > len_max:
        len_max = dist
        max_point = a


print("Координаты наиболее удаленной точки = ", max_point.x, max_point.y)

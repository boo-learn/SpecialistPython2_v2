class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a: Point, b: Point):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


point1 = Point(2, 4)
point2 = Point(5, -2)

print("Расстояние между точками = ", distance(point1, point2))

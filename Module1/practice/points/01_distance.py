class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

point1 = Point(2, 4)
point2 = Point(5, -2)


print("Расстояние между точками = ", distance(point1, point2))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point):
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5


points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
length = 0
for i in points:
    point1 = points[0]
    point2 = points[1]
    length += distance(point1, point2)

print("Длина ломаной линии = ", length)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points1 = Point(2, 4)
point2 = Point(5, -2)


def distance(x, y):
    x = points1.x
    x1 = point2.x
    y = points1.y
    y1 = point2.y
    dist = (((x1 - x) ** 2) + ((y1 - y) ** 2)) ** 0.5
    dist = round(dist, 2)
    return dist
print(distance(points1, point2))

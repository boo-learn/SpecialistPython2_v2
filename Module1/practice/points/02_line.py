import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    dist = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    return dist


points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

broken_len = distance(points[0],points[1])+distance(points[1],points[2])+distance(points[2],points[3])+distance(points[3],points[4])

print("Длина ломаной линии = ", broken_len)

from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

l1 = distance(points[1], points[0])
l2 = distance(points[2], points[1])
l3 = distance(points[3], points[2])
l4 = distance(points[4], points[3])
rez = l1+l2+l3+l4

# Задание: Найдите длину ломаной линии

# TODO: your core here...

print("Длина ломаной линии = ", rez)

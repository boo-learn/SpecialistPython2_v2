from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))


# Дано две точки на координатной плоскости
points1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...

print(distance(points1, point2))

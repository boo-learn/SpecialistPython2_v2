import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        """
        Расстояние между двумя точками
        """
        return math.sqrt(
            math.pow((other_point.x - self.x), 2) +
            math.pow((other_point.y - self.y), 2)
        )


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

prevPoint = None
lineLength = 0

for pt in points:
    if prevPoint is not None:
        lineLength += pt.dist_to(prevPoint)

    prevPoint = pt

print(f"Длина ломаной линии = {lineLength}")

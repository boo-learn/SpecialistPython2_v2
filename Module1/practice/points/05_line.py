import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, p2):
        """
        Расстояние между двумя точками
        """
        return math.sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2)


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
d = 0
# TODO: Найдите длину ломаной линии
for i in range(len(points) - 1):
    p = points[i]
    k = points[i+1]

    d += p.distance_to(k)

print("Длина ломаной линии = ", d)

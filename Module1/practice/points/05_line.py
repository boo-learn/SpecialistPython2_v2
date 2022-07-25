from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self, next_point):
        return sqrt((self.x - next_point.x) ** 2 + (self.y - next_point.y))

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 0), Point(7, 0), Point(5, 0), Point(0, 0), Point(-12, 0)]

len1 = 0
for i in range(len(points) - 1):
    len1 = len1 + points[i].dist(points[i+1])
# TODO: Найдите длину ломаной линии

print("Длина ломаной линии = ", len1)


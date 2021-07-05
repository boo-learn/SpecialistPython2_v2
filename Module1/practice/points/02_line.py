import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

length = 0
prior = Point(0, 0)
for i, point in enumerate(points):
    if i == 0:
        prior = point
    length += point.distance(prior)
    prior = point


print("Длина ломаной линии = ", length)

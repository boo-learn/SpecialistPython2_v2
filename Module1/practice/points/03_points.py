import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

for i, point in enumerate(points):
    if i == 0:
        furthest = point
    else:
        if furthest.distance(Point(0, 0)) < point.distance(Point(0, 0)):
            furthest = point

print(f"Координаты наиболее удаленной точки = {furthest.x}: {furthest.y}")

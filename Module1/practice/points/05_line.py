class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_to(self, another_point):
        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

for point in points:
    i = 0
    while i <= len(points) - 2:
        res2 = 0
        res1 = points[i].dist_to(points[i+1])
        i += 1
        res2 += res1

# TODO: Найдите длину ломаной линии

print("Длина ломаной линии = ", res2)

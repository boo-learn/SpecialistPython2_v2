class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: Найдите длину ломаной линии
    def dist_to(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

lineLength = 0

for i in range(len(points)-1):
    if i < len(points)-1:
        nextPoint = points[i + 1]
        dist = points[i].dist_to(nextPoint)
        lineLength += dist

print("Длина ломаной линии = ", lineLength)

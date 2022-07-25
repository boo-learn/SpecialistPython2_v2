class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.dist_from_0 = (self.x ** 2 + self.y ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

max_x = max_y = 0
max_dist = 0
for point in points:
    if point.dist_from_0 > max_dist:
        max_dist = point.dist_from_0
        max_x, max_y = point.x, point.y

print("Координаты наиболее удаленной точки: x = ", max_x, ", y = ", max_y)

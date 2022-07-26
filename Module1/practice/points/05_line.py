class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Длина ломаной линии
idx = 0
line_len = 0
while idx < len(points) - 1:
    line_len += points[idx].dist_to(points[idx + 1])
    idx += 1

print("Длина ломаной линии = ", line_len)

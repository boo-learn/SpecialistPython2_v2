class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

zero_point = Point(0, 0)
max_dist = 0
longest_point = None

for point in points:
    d = zero_point.dist_to(point)
    if d > max_dist:
        max_dist = d
        longest_point = point

print("Координаты наиболее удаленной точки = ", longest_point.__dict__)

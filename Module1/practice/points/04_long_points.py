class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
zero = Point(0,0)

max_distance = 0
max_point = zero
for point in points:
    distance = point.dist_to(zero)
    if distance > max_distance:
        max_distance = distance
        max_point = point




print("Координаты наиболее удаленной точки = ", max_point.x, max_point.y)

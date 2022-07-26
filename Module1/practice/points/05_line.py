class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5


points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
length = 0
zero_point = points[0]

for point in points:
    length += zero_point.dist_to(point)
    zero_point = point

print("Длина ломаной линии = ", length)

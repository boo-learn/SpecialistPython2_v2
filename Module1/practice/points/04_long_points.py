class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5

zero_point = Point(0, 0)
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
max_dist = 0

for point in points:
    if point.dist_to(zero_point) > max_dist:
        max_dist = point.dist_to(zero_point)
        max_dist_point = point

print(f"Most distant point is ", max_dist_point.x, ",", max_dist_point.y, " at distance of", max_dist)

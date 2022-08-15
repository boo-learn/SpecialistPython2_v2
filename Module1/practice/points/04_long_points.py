class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def max_dist(self, other_point):
        dist = ((self.x-other_point.x)**2 + (self.y-other_point.y)**2)**0.5
        return dist

points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
i = 0
dist_zero_point = 0
dist_all_point = []
zero_point = Point(0, 0)
for point in points:
    dist_zero_point = (Point.max_dist((points[i]), zero_point))
    dist_all_point.append(dist_zero_point)
    i += 1

print("Координаты наиболее удаленной точки = ", max(dist_all_point))

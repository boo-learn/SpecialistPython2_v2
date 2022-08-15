class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5


points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]



summary = sum([points[point].dist_to(points[point + 1]) for point in range(len(points) - 1)])
    

print("Длина ломаной линии = ", summary)

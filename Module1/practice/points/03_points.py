class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

points.insert(0,Point(0,0))

max_dist = 0
large_point = [0,0]
first = points[0]
for point in points[1:]:
    second = point
    dist = distance(first, second)
    if max_dist < dist:
        large_point = point

print("large_point.x, large_point.y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p2.y)**2 ) ** 0.5

points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
random_point = Point(-12, 10)

for point in points:
    print (f"Distance is", distance (point, random_point))

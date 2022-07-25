class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

def distance(p1, p2):
    d = ((point.x - random_point.x) ** 2 + (point.y - random_point.y) ** 2) ** 0.5
    return d


for point in points:
    print(f"(x:{point.x}, y:{point.y})")
    dist = distance(point, random_point)
    print(dist)


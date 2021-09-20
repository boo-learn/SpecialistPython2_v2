class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1,p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** (1 / 2)

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]



max_dist_point = ()
first = Point(0,0)
max_dist = 0
for point in points[1:]:
    second = point
    dist = distance(first, second)
    if max_dist < dist:
        max_dist = dist
        max_dist_point = point



print("Координаты наиболее удаленной точки = ", max_dist_point.x, max_dist_point.y)

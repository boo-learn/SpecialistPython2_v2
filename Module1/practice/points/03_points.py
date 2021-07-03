class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
point_0 = Point(0, 0)
max_dist = 0
for point in points:
    dist_from_0 = distance(point_0, point)
    if dist_from_0 > max_dist:
        max_dist = dist_from_0

print("Координаты наиболее удаленной точки = ", max_dist)

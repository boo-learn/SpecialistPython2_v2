class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

line1 = distance(points[0], points[1])
line2 = distance(points[1], points[2])
line3 = distance(points[2], points[3])
line4 = distance(points[3], points[4])

sum_line = line1 + line2 + line3 + line4
print("Длина ломаной линии = ", sum_line)

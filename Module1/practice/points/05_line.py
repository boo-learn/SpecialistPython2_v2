class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии


def distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)**(0.5)


s = []
for i in range(1, len(points)):
    s.append(distance(points[i - 1], points[i]))


ln = sum(s)
print("Длина ломаной линии = ", ln)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список из произвольного количества точек:
point1 = Point(0, 0)
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
s = []


def distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)**(0.5)


# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
for i in range(len(points)):
    s.append(distance(points[i], point1))

ind = s.index(max(s))

print("Координаты наиболее удаленной точки = ", points[ind].x, ' ', points[ind].y)


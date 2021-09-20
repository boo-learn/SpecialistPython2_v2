class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2, p3, p4, p5):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5 and ((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2) ** 0.5 and ((p3.x - p4.x) ** 2 + (p3.y - p4.y) ** 2) ** 0.5 and ((p4.x - p5.x) ** 2 + (p4.y - p5.y) ** 2) ** 0.5
point1 = Point (2, 4)
point2 = Point (7, 5)
point3 = Point (5, -2)
point4 = Point (0, 6)
point5 = Point (-12, 0)

dist = distance(point1, point2, point3, point4, point5)
# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
# Задание: Найдите длину ломаной линии

# TODO: your core here...

print("Длина ломаной линии = ", dist)

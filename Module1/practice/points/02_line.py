class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """Расстояние между двумя точками"""
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
length = 0
cur_point = points[0]
for next_point in points[1:]:
    length += distance(cur_point, next_point)
    cur_point = next_point


print("Длина ломаной линии = ", length)

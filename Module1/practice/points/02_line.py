import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

line_sum = sum([math.sqrt((points[i + 1].y - points[i].y) ** 2 + (points[i + 1].x - points[i].x) ** 2) for i, _ in
                enumerate(points) if i + 1 != len(points)])
print("Длина ломаной линии = ", line_sum)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

result = 0
for i in range(len(points) - 1):
    result += ((points[i].x - points[i + 1].x) ** 2 + (points[i].y - points[i + 1].y) ** 2) ** (1 / 2)

print("Длина ломаной линии = ", result)

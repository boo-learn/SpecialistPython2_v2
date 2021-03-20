import math


class Point:
    def __init__(self, x, y):  # magic
        self.x = x
        self.y = y

    # функция внутри класса становится МЕТОДОМ
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Ломаная линия задана последовательным списком точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
# индекс   0            1            2             3            4

# Задание: Найдите длину ломаной линии
length = 0
for i in range(len(points) - 1):
    length += points[i].dist(points[i + 1])

# print(dist(Point(12, 4), Point(-5, 4)))

print("Длина ломаной линии = ", length)

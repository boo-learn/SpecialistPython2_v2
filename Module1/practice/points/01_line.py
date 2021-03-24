import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана последовательным списком точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...
length = 0
for i in range(1, len(points)):
    length += math.sqrt((points[i].x - points[i - 1].x) ** 2 + (points[i].y - points[i - 1].y) ** 2)

print("Длина ломаной линии =", length)

#!/usr/bin
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Ломаная линия задана последовательным списком точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...

lst_len = len(points) - 1
final_legth = 0
for i in range(lst_len):
    final_legth += points[i].dist(points[i + 1])

print("Длина ломаной линии = ", final_legth)

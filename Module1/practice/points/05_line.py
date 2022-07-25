import math
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, other_point):
        return math.sqrt((other_point.x-self.x)**2 + (other_point.y-self.y)**2)

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии
vLength = 0

if len(points) > 0:
    for cntr in range(0, len(points) - 1 ):
        vLength += points[cntr].dist_to(points[cntr+1])
        print(points[cntr].dist_to(points[cntr + 1]))

if vLength == 0:
    print("Не удалось определить длинну линии, список точек пуст")
else:
    print("Длина ломаной линии = ", vLength)

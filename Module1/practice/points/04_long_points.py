import math
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, other_point):
        return math.sqrt((other_point.x-self.x)**2 + (other_point.y-self.y)**2)


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
max_distance = -1
max_point = Point(0, 0)


for pnt in points:
    if Point(0, 0).dist_to(pnt) > max_distance:
        max_distance = Point(0, 0).dist_to(pnt)
        max_point = pnt

if max_distance == -1:
    print("Наиболее удалённая точка не определена")
else:
    print("Координаты наиболее удаленной точки: x = ", max_point.x, ", y = ", max_point.y)

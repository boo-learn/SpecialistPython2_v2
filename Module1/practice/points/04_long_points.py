from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты

zero_point = Point(0, 0)

seek_distance = 0

for point in points:
    cur_dist = point.dist_to(zero_point)
    if cur_dist > seek_distance:
        seek_point = point
        seek_distance = cur_dist

print(f"Координаты наиболее удаленной точки = ( {seek_point.x} : {seek_point.y} )  Растояние = {seek_distance:.2f}")

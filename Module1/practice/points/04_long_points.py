from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
point_start = Point(0, 0)
max_point = None
max_dist = 0

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
for p in points:
    distance = point_start.dist_to(p)
    if distance > max_dist:
        max_dist = distance
        max_point = p

print("Наибольшая дистанция = ", max_dist)
print(f"Точка с наибольшей дистанцией = [{max_point.x},{max_point.y}]")


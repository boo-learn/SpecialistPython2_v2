import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, p2):
        """
        Расстояние между двумя точками
        """
        return math.sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2)


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -11), Point(-12, 4)]
zero_point = Point(0, 0)
# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
dist_type = []
for dot in points:
    dist_type.append(dot.distance_to(zero_point))
    if max(dist_type) == dot.distance_to(zero_point):
        output = dot


print(f"Координаты наиболее удаленной точки = {output.x} : {output.y}")

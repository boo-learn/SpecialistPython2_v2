import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        """
        Расстояние между двумя точками
        """
        return math.sqrt(
            math.pow((other_point.x - self.x), 2) +
            math.pow((other_point.y - self.y), 2)
        )


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
# Начало координат
p0 = Point(0, 0)

# Временные переменные результата и дистанции
currMax = 0
result = None

for pt in points:
    dist = pt.dist_to(p0)

    if dist >= currMax:
        result = pt
        currMax = dist

print(f"Координаты наиболее удаленной точки: x = {result.x}, y = {result.y}, distance = {currMax}")

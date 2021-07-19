import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

max_point = max([(math.sqrt((i.y) ** 2 + (i.x) ** 2), i) for i in points])
print(f"Координаты наиболее удаленной точки = {max_point[1].x, max_point[1].y}")

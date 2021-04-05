class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

point_zero = Point(0, 0)

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    import math
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

distances = 0

for point in points:
    if distance(point_zero, point) > distances:
        max_point = point

print("Координаты наиболее удаленной точки = ", max_point.x, max_point.y)

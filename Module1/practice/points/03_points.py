class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

lnt_max = 0
points.insert(0, Point(0, 0))
point_max = 0
for point in points:
    if distance(points[0], point) > lnt_max:
        lnt_max = distance(points[0], point)
        point_max = point

print(f"Координаты наиболее удаленной точки = {point_max.x}, {point_max.y}")
print(f"Растояние состаляет = {lnt_max:.2f}")

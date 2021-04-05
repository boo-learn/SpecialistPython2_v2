class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):  # Расстояние между двумя точками
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
maximum = Point(0, 0)
for point in points:
    if distance(Point(0, 0), maximum) < distance(Point(0, 0), point):
        maximum = point

print(f"Координаты наиболее удаленной точки = {maximum.x}; {maximum.y}")

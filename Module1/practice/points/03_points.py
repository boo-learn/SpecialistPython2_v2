class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1: Point, p2: Point) -> int:
    """
    Расстояние между двумя точками
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

point_null = Point(0, 0)
length = 0.0

for p in points:
    length = max(length, distance(point_null, p))

print("Координаты наиболее удаленной точки = ", length)

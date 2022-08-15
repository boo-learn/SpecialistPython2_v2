class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

zero_point = Point(0, 0)
# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    dists = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    return dists

points_dict = {}

for point in points:
    dist = distance(point, zero_point)  # Передаем объекты point1 и point2 в функцию
    points_dict[point.x, point.y] = dist

reverse_dict = {}
for key, value in points_dict.items():
    reverse_dict[value] = key

max_value = max(reverse_dict.keys())

print("Координаты наиболее удаленной точки = ", reverse_dict[max_value])

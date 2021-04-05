class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** (1 / 2)


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# Задание: Найдите длину ломаной линии
list_lenDist = []
for point in points:
    list_lenDist += [distance(Point(0, 0), point)]

for lenDist in list_lenDist:
    if lenDist == max(list_lenDist):
        print(f"Координаты наиболее удаленной точки = ({points[list_lenDist.index(lenDist)].x}, {points[list_lenDist.index(lenDist)].y})")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2) -> float:
    """
    Расстояние между двумя точками
    """
    return round(((point1.x - point2.x) ** 2 +
                  (point1.y - point2.y) ** 2) ** 0.5, 2)


def find_max(points) -> tuple:
    """
    Находит координаты наиболее удаленной точки от начала координат
    :param points:
    :return:
    """
    start_point = Point(0, 0)
    max_length = 0
    result = 0
    for point in points:
        if (dist := distance(point, start_point)) > max_length:
            max_length, result = dist, point
    return result.x, result.y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
print("Координаты наиболее удаленной точки = ", find_max(points))

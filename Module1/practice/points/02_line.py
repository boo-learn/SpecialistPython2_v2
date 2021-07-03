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


def length(points) -> float:
    """
    :param points: Координаты точек, составляющих линию
    :return: Длина линии
    """
    result = 0
    for i in range(1, len(points)):
        result += distance(points[i-1], points[i])
    return result


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

print("Длина ломаной линии = ", length(points))

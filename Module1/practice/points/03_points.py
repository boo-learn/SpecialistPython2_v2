from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """Расстояние между двумя точками"""
    return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

def find_most_distanced_point(points: list) -> Point:
    """Получает список точек и возвращает наиболее удалённую отначала координат"""
    maxed_point = Point(0, 0)
    root_point = Point(0, 0)
    for point in points:
        if distance(point, root_point) > distance(maxed_point, root_point):
            maxed_point = point
    return maxed_point


if __name__ == '__main__':
    maxed_point = find_most_distanced_point(points)
    print(f"Координаты наиболее удаленной точки = {maxed_point.x}:{maxed_point.y}")

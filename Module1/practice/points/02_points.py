import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(points, random_point):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    for point in points:
        print(math.sqrt(((point.x - random_point.x) ** 2) + ((point.y - random_point.y) ** 2)))


def main():
    # Дан список из произвольного количества точек:
    points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
    # И произвольная точка на плоскости:
    random_point = Point(-12, 10)
    distance(points, random_point)


if __name__ == "__main__":
    main()

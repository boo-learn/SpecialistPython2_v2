import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


def dist_to(points):
    list_points = []

    for point in points:
        list_points.append(math.sqrt(((0 - point.x) ** 2) + ((0 - point.y) ** 2)))
    return list_points


# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
def main():
    print("Координаты наиболее удаленной точки = ", max(dist_to(points)))


if __name__ == '__main__':
    main()

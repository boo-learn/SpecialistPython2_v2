import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return math.sqrt(((p1.x -p2.x) ** 2) + ((p1.y - p2.y) ** 2))
    # TODO: напишите тело функции


def main():
    point1 = Point(2, 4)
    point2 = Point(5, -2)

    dist = distance(point1, point2)  # Передаем объекты point1 и point2 в функцию

    return f"Расстояние между точками = {dist}"


if __name__ == "__main__":
    sys.exit(main())

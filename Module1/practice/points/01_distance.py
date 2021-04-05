from math import sqrt


class Point:
    """Точка в двоичной системе координат"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """Расстояние между двумя точками"""
    return round(sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2), 2)


if __name__ == '__main__':
    # Дано две точки на координатной плоскости
    point1 = Point(2, 4)
    point2 = Point(5, -2)

    # Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
    res = distance(point1, point2)

    print(f"Расстояние между точками = {res}")

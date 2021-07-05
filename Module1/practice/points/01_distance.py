class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(pt1: Point, pt2: Point):
    """
    Расстояние между двумя точками
    """
    return ((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2)**0.5


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...


print("Расстояние между точками = ", distance(point1, point2))

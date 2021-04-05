class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """

    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

d = distance(point1, point2)

print("Расстояние между точками = ", d)

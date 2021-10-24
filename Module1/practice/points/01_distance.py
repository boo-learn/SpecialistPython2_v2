class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a, b):
    """
    Расстояние между двумя точками
    """
    ab = ((b.x - a.x)**2 + (b.y - a.y)**2)**0.5
    return ab


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...


print("Расстояние между точками = ", distance(point1, point2))

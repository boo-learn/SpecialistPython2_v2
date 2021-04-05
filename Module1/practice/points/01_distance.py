class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2):
    """
    Расстояние между двумя точками
    """
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5


# Даны две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найти расстояние между этими точками, реализовав и используя функцию distance()
print("Расстояние между точками = ", distance(point1, point2))

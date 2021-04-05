class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p_1, p_2):
    """
    Расстояние между двумя точками
    """
    return ((p_2.x - p_1.x) ** 2 + (p_2.y - p_1.y) ** 2) ** (1/2)


# Дано две точки на координатной плоскости
point_1 = Point(0, 0)
point_2 = Point(3, 4)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

print(f"Расстояние между точками = {distance(point_1, point_2)}")

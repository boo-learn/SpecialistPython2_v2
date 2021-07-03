class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(fv_p1, fv_p2):
    """
    Расстояние между двумя точками
    """
    return((fv_p1.x - fv_p2.x)**2 + (fv_p1.y - fv_p2.y)**2)**0.5

# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

lenght = distance(point1, point2)
print("Расстояние между точками = ", lenght)
